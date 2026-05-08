# IT-Helpdesk-Analytics
End-to-end IT helpdesk analytics using Python, MySQL &amp; Power BI

# 🖥️ IT Helpdesk Analytics Dashboard

An end-to-end data analytics project analyzing IT support operations
using Python, MySQL, and Power BI.

---

## 📌 Problem Statement

IT support teams often lack visibility into ticket trends, agent
performance, and SLA compliance. Without data-driven insights,
managers cannot identify bottlenecks or allocate resources effectively.

This project builds a complete analytics pipeline that transforms
raw helpdesk data into actionable business insights.

---

## 🛠️ Tools & Technologies

| Tool       | Purpose                              |
|------------|--------------------------------------|
| Python     | Data generation, cleaning, loading   |
| MySQL      | Data storage, querying, views        |
| Power BI   | Interactive dashboard, KPIs          |
| Pandas     | Data manipulation                    |
| SQLAlchemy | Python-MySQL connection              |
| Faker      | Realistic data generation            |

---

## 📊 Dashboard Preview
<img width="981" height="557" alt="dashboard_agents" src="https://github.com/user-attachments/assets/44a79148-3cc9-478b-82d1-d20d742a7311" />
<img width="981" height="549" alt="dashboard_trends" src="https://github.com/user-attachments/assets/66ee8deb-e10e-41d5-b8b8-48ef6fc8485e" />
<img width="983" height="555" alt="dashboard_overview" src="https://github.com/user-attachments/assets/e45e350f-ff69-4f2a-8357-71140b3fed5b" />


## 🔍 Key Insights Discovered


- 📌 **Overall SLA breach rate: 0.25% approx** — Software category had
  the highest breach rate at 0.3%
- 📌 **Agent Priya singh resolved tickets 3.29% faster** than average
  with lowest breach rate of 25.38%
- 📌 **Critical tickets in Legal department** had the highest
  breach rate at 1% — a major risk area
- 📌 **Email issues** take longest to resolve at avg 32.45 hours

---






---

## ⚙️ How to Run This Project

### Prerequisites
- Python 3.11+
- MySQL 8.0+
- Power BI Desktop

### Step 1 — Install Python libraries
```bash
pip install pandas numpy faker sqlalchemy pymysql
```

### Step 2 — Generate data
```bash
python data_generation.py
```

### Step 3 — Clean data
```bash
python data_cleaning.py
```

### Step 4 — Load into MySQL
Update credentials in `load_to_mysql.py` then run:
```bash
python load_to_mysql.py
```

### Step 5 — Run SQL queries
Open `sql/analysis_queries.sql` in MySQL Workbench and execute

### Step 6 — Open Dashboard
Open `powerbi/IT_Dashboard.pbix` in Power BI Desktop

---

## 📈 Dataset Details

| Field              | Description                          |
|--------------------|--------------------------------------|
| ticket_id          | Unique ticket identifier             |
| category           | Type of IT issue                     |
| priority           | Low / Medium / High / Critical       |
| status             | Open / In Progress / Resolved /Closed|
| department         | Department that raised ticket        |
| assigned_agent     | IT agent handling ticket             |
| created_date       | When ticket was raised               |
| resolved_date      | When ticket was resolved             |
| resolution_hours   | Time taken to resolve                |
| sla_breached       | Whether SLA was breached Yes/No      |
| is_weekend         | Was ticket raised on weekend         |
| resolution_bucket  | Speed category of resolution         |

---

## 💡 Skills Demonstrated

- ✅ Python data generation and cleaning
- ✅ Feature engineering
- ✅ MySQL database design and querying
- ✅ Advanced SQL — Window functions, CASE WHEN, Views
- ✅ Power BI dashboard development
- ✅ DAX measures and calculated columns
- ✅ Business KPI definition and analysis
- ✅ Data storytelling and insight generation

