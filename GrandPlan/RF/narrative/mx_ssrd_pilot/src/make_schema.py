#!/usr/bin/env python3
"""Generate schema/mx_ssrd.schema.json (JSON Schema draft 2020-12).

The 31 GPRD core names are WP/26/236 Stage 1/2 names, verbatim. Multi-value GPRD
fields are arrays of enums here so every controlled value is enumerated;
flatten.py joins them with ';' to recover the GPRD cell format.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEM = "Not explicitly mentioned"
MMYYYY = f"^((0[1-9]|1[0-2])-[0-9]{{4}}|{NEM})$"
DDMMYYYY = f"^((0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-[0-9]{{4}}|{NEM})$"


def enum(*values):
    return {"type": "string", "enum": list(values)}


def many(*values):
    return {"type": "array", "items": enum(*values), "minItems": 1, "uniqueItems": True}


TEXT = {"type": "string"}
DATE = {"type": "string", "pattern": MMYYYY}

CORE = {
    "Country Name": TEXT,
    "Year of the article": {"type": "string", "pattern": f"^([0-9]{{4}}|{NEM})$"},
    "Status of Pension Reform": many("Legislated", "Planned", "Announced", "Implemented", "Reversed", "Other"),
    "legislation_date": DATE,
    "Planned_date": DATE,
    "announcement_date": DATE,
    "implementation_date": DATE,
    "reversal_date": DATE,
    "Pension Reform Types": many(
        "indexation", "coverage", "benefit rule changes", "systematic (structural) pension reforms",
        "funding mechanisms", "retirement age", "pension portability", "investment strategies",
        "administration and governance", "sustainability and solvency measures", "pension plan types",
        "eligibility and access", "others", NEM),
    "indexation_change": enum("more generous indexation", "less generous indexation", NEM),
    "coverage_change": enum("extended coverage", "reduced coverage", NEM),
    "benefit_change": enum("more generous benefits", "less generous benefits", NEM),
    "Social_insurance_change": enum("Yes", "No", NEM),
    "Reform_category": enum("Parametric reform", "Structural reform", NEM),
    "reform_coverage": enum("Targeted reform", "Broad-based reform", "Mixed", NEM),
    "reason_reform": many(
        "Economic growth", "Fiscal reasons", "Benefit adequacy", "Distributional impact", "Economic impact",
        "Inflation", "Demographic changes", "Inequality and fairness", "Labor market changes", "Other", NEM),
    "relevancetopr_score": {"type": "number", "minimum": 0, "maximum": 10},
    "retirement_age_change": enum("retirement age increased", "retirement age decreased", NEM),
    "Retirement_age_change_details": TEXT,
    "Retirement_age_pre_reform_female": TEXT,
    "Retirement_age_after_reform_female": TEXT,
    "Retirement_age_pre_reform_male": TEXT,
    "Retirement_age_after_reform_male": TEXT,
    "Contribution_rate_change": enum("contribution rate increased", "contribution rate decreased", NEM),
    "Old Employer Contribution Rate": TEXT,
    "New Employer Contribution Rate": TEXT,
    "Old Employee Contribution Rate": TEXT,
    "New Employee Contribution Rate": TEXT,
    "Old Contribution Rate (Employee and Employer Combined)": TEXT,
    "New Contribution Rate (Employee and Employer Combined)": TEXT,
    "Is the legislated pension reform minor or major?": enum("Minor", "Major", "N/A"),
}
assert len(CORE) == 31

EXT = {
    "instrument_type": enum("constitutional_reform", "new_law", "law_reform", "decree", "regulation",
                            "technical_council_agreement", "administrative_rule", "other"),
    "issuing_body": TEXT,
    "dof_publication_date": {"type": "string", "pattern": DDMMYYYY},
    "entry_into_force_date": {"type": "string", "pattern": DDMMYYYY},
    "legal_references": {"type": "array", "items": TEXT},
    "regime_affected": many("ley73", "ley97", "issste_decimo_transitorio", "issste_2007_accounts",
                            "non_contributory", "imss_staff_rjp", "all", "other"),
    "insurance_branch": many("IV", "RCV", "SEM", "SEM_pensioners_GMP", "RT", "GPS", "infonavit",
                             "non_contributory_pension", "other"),
    "financing_indexation_change": enum("changed_to_uma", "changed_to_wage", "changed_to_inflation", "other", NEM),
    "fiscal_magnitude_stated": TEXT,
    "implicit_liability_direction": enum("increases", "decreases", "ambiguous", NEM),
}
FIELDS = list(CORE) + list(EXT)
FIELD = enum(*FIELDS)
TAIL = {
    "fields_inferred": {"type": "array", "items": FIELD, "uniqueItems": True},
    "evidence": {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {"field": FIELD, "quote": TEXT, "location": TEXT},
            "required": ["field", "quote", "location"],
            "additionalProperties": False,
        },
    },
    "source_file": TEXT,
    "chunk_ids": {"type": "array", "items": TEXT},
}
props = {**CORE, **EXT, **TAIL}
schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "mx_ssrd.schema.json",
    "title": "MX-SSRD episode record (GPRD 31 core fields plus Mexican extensions)",
    "type": "object",
    "properties": props,
    "required": list(props),
    "additionalProperties": False,
}
path = os.path.join(ROOT, "schema", "mx_ssrd.schema.json")
json.dump(schema, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(len(CORE), "core +", len(EXT) + len(TAIL), "extension fields ->", path)
