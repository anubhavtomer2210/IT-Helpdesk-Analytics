import pandas as pd
import numpy as np

# ─────────────────────────────────────────
# STEP 1 — LOAD THE RAW DATA
# ─────────────────────────────────────────
df = pd.read_csv('data/raw_tickets.csv')

print("✅ Raw Data Loaded")
print(f"Shape: {df.shape}")
print("\nFirst 5 rows:")
print(df.head())

# ─────────────────────────────────────────
# STEP 2 — BASIC INSPECTION
# ─────────────────────────────────────────
print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Duplicate Rows ---")
print(f"Total duplicates: {df.duplicated().sum()}")

# ─────────────────────────────────────────
# STEP 3 — FIX DATA TYPES
# ─────────────────────────────────────────

# Convert date columns from text to proper datetime format
df['created_date']  = pd.to_datetime(df['created_date'])
df['resolved_date'] = pd.to_datetime(df['resolved_date'])

print("\n✅ Date columns converted to datetime")

# ─────────────────────────────────────────
# STEP 4 — HANDLE MISSING VALUES
# ─────────────────────────────────────────

# Check which columns have nulls
print("\n--- Missing Values Before Handling ---")
print(df.isnull().sum())

# resolved_date, resolution_hours, sla_breached are NULL for open tickets
# This is VALID missing data — we do not fill or drop these
# We just document them clearly

# Fill sla_breached nulls with 'Pending' for open/in-progress tickets
df['sla_breached'] = df['sla_breached'].fillna('Pending')

# Keep resolution_hours as NULL — we cannot fake a resolution time
# Keep resolved_date as NULL — ticket is not resolved yet

print("\n--- Missing Values After Handling ---")
print(df.isnull().sum())

# ─────────────────────────────────────────
# STEP 5 — REMOVE DUPLICATES
# ─────────────────────────────────────────
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]
print(f"\n✅ Duplicates removed: {before - after} rows dropped")

# ─────────────────────────────────────────
# STEP 6 — FEATURE ENGINEERING
# ─────────────────────────────────────────

# Extract useful time-based columns from created_date
df['created_year']  = df['created_date'].dt.year
df['created_month'] = df['created_date'].dt.month
df['created_month_name'] = df['created_date'].dt.strftime('%B')  # January, February...
df['created_day']   = df['created_date'].dt.day_name()           # Monday, Tuesday...
df['created_hour']  = df['created_date'].dt.hour                 # 0 to 23

# Categorize resolution time into buckets
def resolution_bucket(hours):
    if pd.isnull(hours):
        return 'Pending'
    elif hours <= 4:
        return 'Very Fast (0-4 hrs)'
    elif hours <= 24:
        return 'Fast (4-24 hrs)'
    elif hours <= 48:
        return 'Medium (24-48 hrs)'
    else:
        return 'Slow (48+ hrs)'

df['resolution_bucket'] = df['resolution_hours'].apply(resolution_bucket)

# Flag high priority SLA breaches — most critical for business
df['critical_breach'] = (
    (df['priority'] == 'Critical') & (df['sla_breached'] == 'Yes')
).astype(int)  # 1 = yes, 0 = no

print("\n✅ Feature engineering done")
print(f"New columns added: created_year, created_month, created_month_name,")
print(f"                   created_day, created_hour, resolution_bucket, critical_breach")

# ─────────────────────────────────────────
# STEP 7 — STANDARDIZE TEXT COLUMNS
# ─────────────────────────────────────────

# Remove extra spaces and fix capitalization in text columns
text_columns = ['category', 'priority', 'status', 'department',
                'assigned_agent', 'sla_breached', 'is_weekend']

for col in text_columns:
    df[col] = df[col].str.strip()   # remove leading/trailing spaces
    df[col] = df[col].str.title()   # Title Case each value

print("\n✅ Text columns standardized")

# ─────────────────────────────────────────
# STEP 8 — FINAL CHECK
# ─────────────────────────────────────────
print("\n--- Final Dataset Info ---")
print(f"Shape: {df.shape}")
print(f"\nColumns: {list(df.columns)}")
print(f"\nData Types:\n{df.dtypes}")
print(f"\nSample Data:\n{df.head(3)}")

# ─────────────────────────────────────────
# STEP 9 — SAVE CLEANED DATA
# ─────────────────────────────────────────
df.to_csv('data/cleaned_tickets.csv', index=False)
print("\n✅ Cleaned data saved to data/cleaned_tickets.csv")