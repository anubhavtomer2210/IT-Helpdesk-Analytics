import pandas as pd
from sqlalchemy import create_engine, text

# ─────────────────────────────────────────
# STEP 1 — DATABASE CONNECTION
# ─────────────────────────────────────────


USERNAME = 'root'        
PASSWORD = 'password'  
HOST     = 'localhost'
PORT     = '3306'
DATABASE = 'it_helpdesk'

# Create connection engine
engine = create_engine(
    f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}',
    echo=False
)

print("✅ Connection engine created")

# ─────────────────────────────────────────
# STEP 2 — CREATE DATABASE IF NOT EXISTS
# ─────────────────────────────────────────

# Connect without specifying database first
base_engine = create_engine(
    f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}',
    echo=False
)

with base_engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS it_helpdesk"))
    conn.commit()

print("✅ Database 'it_helpdesk' ready")

# ─────────────────────────────────────────
# STEP 3 — LOAD CLEANED CSV
# ─────────────────────────────────────────

df = pd.read_csv('data/cleaned_tickets.csv')

# Convert date columns back to datetime after reading csv
df['created_date']  = pd.to_datetime(df['created_date'])
df['resolved_date'] = pd.to_datetime(df['resolved_date'])

print(f"✅ CSV loaded — {df.shape[0]} rows, {df.shape[1]} columns")

# ─────────────────────────────────────────
# STEP 4 — LOAD INTO MYSQL TABLE
# ─────────────────────────────────────────

df.to_sql(
    name='tickets',        # table name in MySQL
    con=engine,
    if_exists='replace',   # drop and recreate if table already exists
    index=False,           # don't write dataframe index as a column
    chunksize=1000         # insert 1000 rows at a time
)

print("✅ Data loaded into MySQL table 'tickets'")

# ─────────────────────────────────────────
# STEP 5 — VERIFY DATA IN MYSQL
# ─────────────────────────────────────────

with engine.connect() as conn:

    # Count rows
    result = conn.execute(text("SELECT COUNT(*) FROM tickets"))
    count  = result.fetchone()[0]
    print(f"\n✅ Total rows in MySQL: {count}")

    # Preview first 3 rows
    result = conn.execute(text("SELECT * FROM tickets LIMIT 3"))
    rows   = result.fetchall()
    print("\n--- First 3 rows from MySQL ---")
    for row in rows:
        print(row)