# Tests for the §11 acceptance criteria of design note B0 v1.2 that code can check.
# Run:  julia --project=. test/runtests.jl     (from GrandPlan/Aurora/crypto_abm)
using Test, Random, Statistics, Dates
using CryptoABM
using CryptoABM.ABMCore, CryptoABM.Moments, CryptoABM.CryptoAdapter
const ROOT = normpath(joinpath(@__DIR__, ".."))
include(joinpath(ROOT, "targets", "Targets.jl")); using .Targets

const SIGBAR = Targets.sigma_bar_hourly().σbar

function run_path(p::Params; seed = 1, days = 1040, burnin = 120, cascade = true)
    rng = Xoshiro(seed)
    w = build_world(p, rng)
    res = simulate!(w, SimConfig(K = p.K, days = days, burnin = burnin, cascade = cascade), rng)
    w, res
end
logret(res) = diff(log.(res.close))

@testset "B1a acceptance tests" begin

    @testset "1 layout: no crypto terms in src/core" begin
        bad = r"\b(funding|perp\w*|btc|bitcoin|eth|ether|ethereum|coinbase|utc|crypto\w*|stablecoin\w*)\b"i
        for f in readdir(joinpath(ROOT, "src", "core"); join = true)
            endswith(f, ".jl") || continue
            for (k, ln) in enumerate(eachline(f))
                @test !occursin(bad, ln) || (println("crypto term in $(basename(f)):$k: ", ln); false)
            end
        end
        for f in ("src/core/ABMCore.jl", "src/core/Moments.jl", "src/adapters/crypto/CryptoAdapter.jl",
                  "targets/Targets.jl")
            @test isfile(joinpath(ROOT, replace(f, ".jl" => ".md")))
        end
    end

    @testset "2 targets reproduce note §1.1 from the committed snapshot" begin
        @test Targets.verify_snapshot()
        s = Targets.window_stats("BTC-USD", Targets.POST...)
        @test s.n == 1040
        @test round(100s.sd; digits = 2) == 2.46
        @test round(s.exkurt; digits = 2) == 3.44
        @test round(s.hill; digits = 2) == 3.45
        @test round(100s.three_sigma; digits = 2) == 1.92
        x = Targets.window_stats("BTC-USD", Targets.PRE...; exclude = Date(2020, 3, 12))
        @test round(x.exkurt; digits = 2) == 3.56
        @test round(x.skew; digits = 2) == 0.03
        e = Targets.window_stats("ETH-USD", Targets.POST...)
        @test round(100e.sd_ann; digits = 1) == 67.0
    end

    @testset "3 null test: noise only, κ = 0" begin
        p = Params(w_c = 0, w_m = 0, w_l = 0, κ = 0.0, σbar = SIGBAR)
        ks = Float64[]; a1 = Float64[]
        for seed in 1:5
            _, res = run_path(p; seed)
            r = logret(res)
            push!(ks, exkurt(r)); push!(a1, acf(abs.(r), 1))
        end
        @test abs(mean(ks)) < 0.25
        @test abs(mean(a1)) < 0.05
    end

    @testset "7 determinism and conservation" begin
        p = Params(σbar = SIGBAR)
        w1, r1 = run_path(p; seed = 42, days = 300)
        w2, r2 = run_path(p; seed = 42, days = 300)
        @test r1.close == r2.close          # bit-identical
        @test r1.low == r2.low
        # units: classes + LP inventory = initial units (conviction holdings)
        units = sum(units_held, w1.classes) + w1.lp.inventory
        @test isapprox(units, p.w_c; atol = 1e-10)
        # cash: classes + LP + loss fund − external injections = 0 (start from zero cash)
        cash = sum(cash_held, w1.classes) + w1.lp.cash + w1.fund.balance - w1.ledger.cash_in
        @test isapprox(cash, 0.0; atol = 1e-9)
    end

    @testset "R4 cascade cap never binds; rounds recorded" begin
        p = Params(σbar = SIGBAR)
        w, res = run_path(p; seed = 7, days = 400)
        N = sum(n_constrained, w.classes)
        @test res.max_rounds <= N + 1
    end

    @testset "R5 core stubs" begin
        iss = Issuer(10.0, 0.95)
        filled, px = primary_auction(iss, [(1.0, 4.0), (0.97, 4.0), (0.90, 10.0)])
        @test filled == 8.0 && px == 0.97                # uncovered: 8 of 10, bids below 0.95 rejected
        cal = EventCalendar([Event(5, :maturity, 1, 1.0), Event(9, :coupon, 1, 0.02)])
        @test length(events_at(cal, 5)) == 1 && isempty(events_at(cal, 6))
        c = StateConstraint(s -> s.equity < s.margin)
        @test breached(c, (equity = 1.0, margin = 2.0)) && !breached(c, (equity = 3.0, margin = 2.0))
        @test isempty(consol(:x).cashflows)
    end

    @testset "9 firewall: crypto_abm code never touches crypto_monitor" begin
        for (dir, _, files) in walkdir(ROOT), f in files
            any(endswith(f, e) for e in (".jl", ".py", ".toml", ".sh")) || continue
            occursin("runtests.jl", f) && continue      # this file names the board only to test for it
            txt = read(joinpath(dir, f), String)
            @test !occursin("crypto_monitor", txt) || (println("firewall breach: ", joinpath(dir, f)); false)
        end
    end
end
