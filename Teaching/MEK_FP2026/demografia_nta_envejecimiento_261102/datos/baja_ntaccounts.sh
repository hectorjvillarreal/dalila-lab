#!/usr/bin/env bash
# Baja perfiles por edad de la base pública de NTA (ntaccounts.org) con el formulario de "Browse database".
# El servidor exige el encabezado Referer que manda un navegador. Salida: ntaccounts_perfiles.csv y ntaccounts_documentacion.csv.
set -euo pipefail
cd "$(dirname "$0")"
TMP=$(mktemp -d); B=https://ntaccounts.org/web/nta; R=$B/download-confirm
ARGS=()
for c in Mexico Brazil "Costa Rica" Chile Colombia Peru Uruguay Argentina Germany Sweden Japan Philippines "United States of America" "South Korea"; do ARGS+=(--data-urlencode "countries=$c"); done
for v in "Consumption" "Labor Income" "LifeCycle Deficit" "Public Consumption" "Public Consumption, Health" "Public Consumption, Education" "Private Consumption" "Private Consumption, Health" "Private Consumption, Education" "Public Transfers" "Public Transfers, Inflows" "Public Transfers, Outflows" "Public Transfers, Health, Inflows" "Public Transfers, Education, Inflows" "Public Transfers, Pensions, Inflows" "Public Transfers, Other In-Kind, Inflows" "Public Transfers, Other Cash, Inflows" "Private Transfers" "Intrahousehold Transfers" "Interhousehold Transfers" "Asset-based Reallocations" "Public Asset-based Reallocations" "Private Asset-based Reallocations" "UN Population, Total" "Support Ratio" "Fiscal Support Ratio"; do ARGS+=(--data-urlencode "var-names=$v"); done
for t in "Smooth Mean" "Mean"; do ARGS+=(--data-urlencode "var-types=$t"); done
curl -sSL -m 90 -c $TMP/j -b $TMP/j -o $TMP/c.html "$R" "${ARGS[@]}" --data-urlencode 'submit=Submit'
python3 -I - "$TMP/c.html" > $TMP/u <<'P'
import re,sys
h=open(sys.argv[1],encoding='utf8',errors='ignore').read()
a=re.findall(r"<form method='POST' action='([^']+)'>\s*<input type='submit' class='down-button' name='submit' value='([^']+)'",h)
print(len(a),file=sys.stderr); print(a[0][0]); print(a[2][0])
P
U1=$(sed -n 1p $TMP/u); U2=$(sed -n 2p $TMP/u)
curl -sSL -m 120 -b $TMP/j -e "$R" -o ntaccounts_perfiles.csv -d submit=Download "https://ntaccounts.org$U1"
curl -sSL -m 120 -b $TMP/j -e "$R" -o ntaccounts_documentacion.csv -d submit=Download "https://ntaccounts.org$U2"
