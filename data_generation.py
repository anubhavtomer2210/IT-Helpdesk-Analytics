import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()
random.seed(42)
np.random.seed(42)

# ─────────────────────────────────────────
# SETTINGS — you can change these values
# ─────────────────────────────────────────
NUM_TICKETS = 10000

CATEGORIES   = ['Hardware', 'Software', 'Network', 'Access/Login', 'Email', 'Printer']
PRIORITIES   = ['Low', 'Medium', 'High', 'Critical']
STATUSES     = ['Resolved', 'Closed', 'Open', 'In Progress']
DEPARTMENTS  = ['HR', 'Finance', 'Sales', 'IT', 'Operations', 'Marketing', 'Legal']
AGENTS       = ['Amit Sharma', 'Priya Singh', 'Rohit Verma',
                'Neha Gupta', 'Suresh Kumar', 'Anjali Mehta', 'Vikram Joshi']

# SLA limits in hours per priority
SLA_LIMITS = {
    'Low': 72,
    'Medium': 48,
    'High': 24,
    'Critical': 4
}

# ─────────────────────────────────────────
# GENERATE DATA
# ─────────────────────────────────────────
records = []

for i in range(1, NUM_TICKETS + 1):

    # Basic fields
    ticket_id   = f'TKT-{i:05d}'
    category    = random.choice(CATEGORIES)
    priority    = random.choices(PRIORITIES, weights=[30, 40, 20, 10])[0]
    status      = random.choices(STATUSES,   weights=[50, 30, 10, 10])[0]
    department  = random.choice(DEPARTMENTS)
    agent       = random.choice(AGENTS)

    # Dates — tickets created between Jan 2023 and Dec 2024
    created_date = fake.date_time_between(
        start_date=datetime(2023, 1, 1),
        end_date=datetime(2024, 12, 31)
    )

    # Resolution time depends on priority
    base_hours = {
        'Low': random.randint(10, 90),
        'Medium': random.randint(5, 60),
        'High': random.randint(2, 30),
        'Critical': random.randint(1, 10)
    }
    resolution_hours = base_hours[priority]

    # If ticket is still open/in-progress, no resolved date
    if status in ['Open', 'In Progress']:
        resolved_date    = None
        resolution_hours = None
        sla_breached     = None
    else:
        resolved_date = created_date + timedelta(hours=resolution_hours)
        sla_limit     = SLA_LIMITS[priority]
        sla_breached  = 'Yes' if resolution_hours > sla_limit else 'No'

    # Was ticket raised on weekend?
    is_weekend = 'Yes' if created_date.weekday() >= 5 else 'No'

    records.append({
        'ticket_id'       : ticket_id,
        'category'        : category,
        'priority'        : priority,
        'status'          : status,
        'department'      : department,
        'assigned_agent'  : agent,
        'created_date'    : created_date,
        'resolved_date'   : resolved_date,
        'resolution_hours': resolution_hours,
        'sla_breached'    : sla_breached,
        'is_weekend'      : is_weekend
    })

# ─────────────────────────────────────────
# SAVE TO CSV
# ─────────────────────────────────────────
df = pd.DataFrame(records)
df.to_csv('data/raw_tickets.csv', index=False)

print(f"✅ Done! {NUM_TICKETS} tickets generated.")
print(df.head())
print(df.shape)