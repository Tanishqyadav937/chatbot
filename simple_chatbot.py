import pandas as pd
import re
import json
from pathlib import Path

# ---------- Config ----------
DATA_PATH = Path("final_financials_analysis.xlsx")   # produced earlier
RULES_PATH = Path("rules_financial_faq.json")
# ----------------------------

# Load data
df = pd.read_excel(DATA_PATH)
# normalize Company names for matching
df['Company_norm'] = df['Company'].str.lower().str.strip()

# Load rules
with open(RULES_PATH, 'r') as f:
    rules = json.load(f)

# Helper functions
def normalize_text(s):
    return s.lower().strip()

COMPANIES = df['Company_norm'].unique().tolist()
METRIC_MAP = {
    'revenue': 'Total Revenue (USD mn)',
    'total revenue': 'Total Revenue (USD mn)',
    'net income': 'Net Income (USD mn)',
    'assets': 'Total Assets (USD mn)',
    'total assets': 'Total Assets (USD mn)',
    'liabilities': 'Total Liabilities (USD mn)',
    'cash flow': 'Cash Flow from Ops (USD mn)',
    'cash flow from ops': 'Cash Flow from Ops (USD mn)',
    'profit margin': 'Profit Margin (%)',
    'debt to assets': 'Debt-to-Assets Ratio',
    'debt-to-assets': 'Debt-to-Assets Ratio'
}

def extract_company(text):
    text_l = normalize_text(text)
    for c in COMPANIES:
        if c in text_l:
            return c.title()
    return None

def extract_year(text):
    m = re.search(r'\b(20\d{2})\b', text)
    if m:
        return int(m.group(1))
    return None

def extract_metric(text):
    text_l = normalize_text(text)
    for key in METRIC_MAP.keys():
        if key in text_l:
            return METRIC_MAP[key], key
    return None, None

def get_value(company, year, metric_col):
    row = df[(df['Company'].str.lower() == company.lower()) & (df['Fiscal Year'] == year)]
    if row.empty:
        return None
    val = row.iloc[0].get(metric_col, None)
    return val

def compute_pct_change(company, metric_col, from_year, to_year):
    v1 = get_value(company, from_year, metric_col)
    v2 = get_value(company, to_year, metric_col)
    if v1 in (None, 0) or v2 is None:
        return None
    return (v2 - v1) / abs(v1) * 100

def handle_query(text):
    text_n = normalize_text(text)
    # Extract common slots
    company = extract_company(text)
    year = extract_year(text)
    metric_col, metric_key = extract_metric(text)
    # try specific intents
    # 1) metric by company and year
    if company and year and metric_col:
        val = get_value(company, year, metric_col)
        if val is not None:
            # format numeric nicely
            if '(%' in metric_col or 'Ratio' in metric_col:
                return f"{company} {metric_key} in {year} was {val:.2f}."
            else:
                return f"{company} {metric_key} in {year} was {val:,.0f} (USD mn)."
    # 2) YoY growth (two years)
    years = re.findall(r'\b(20\d{2})\b', text)
    if company and metric_col and len(years) >= 2:
        y1, y2 = int(years[0]), int(years[1])
        pct = compute_pct_change(company, metric_col, y1, y2)
        if pct is not None:
            return f"{company}'s {metric_key} growth from {y1} to {y2} was {pct:.2f}%."
    # 3) Compare revenue for a year
    if 'compare revenue' in text_n or ('highest revenue' in text_n and year):
        # rank companies by revenue in year
        rows = df[df['Fiscal Year'] == year][['Company','Total Revenue (USD mn)']].sort_values('Total Revenue (USD mn)', ascending=False)
        if rows.empty:
            return f"No revenue data found for {year}."
        ranked = ", ".join([f"{r.Company} ({int(r['Total Revenue (USD mn)']):,d})" for r in rows.itertuples()])
        return f"In {year}, revenue ranking (desc) was: {ranked}."
    # fallback
    return "I couldn't map that to a predefined question. Try: 'What was Apple revenue in 2024?' or 'Profit margin Tesla 2023'."

# Quick CLI test
if __name__ == "__main__":
    print(handle_query("What was Microsoft total revenue in 2024?"))
    print(handle_query("What is Tesla profit margin in 2024?"))
    print(handle_query("Compare revenue for 2024"))
    print(handle_query("What was Apple's cash flow in 2023?"))

import pandas as pd
from pathlib import Path

DATA_PATH = Path("final_financials_analysis.xlsx")
xls = pd.ExcelFile(DATA_PATH, engine='openpyxl')
print(xls.sheet_names)
