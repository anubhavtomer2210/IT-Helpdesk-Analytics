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
[IT_Dashboard.pdf](https://github.com/user-attachments/files/27564713/IT_Dashboard.pdf)



## 🔍 Key Insights Discovered


📌 The organization recorded an overall SLA breach rate of approximately 20%, meaning nearly 1 out of every 5 tickets failed to meet the expected resolution timeline.

📌Critical-priority tickets in the Legal department showed an SLA breach rate of nearly 48%, the highest among all department-priority combinations.

📌Email-related tickets had the highest average resolution time at 32.45 hours, indicating workflow bottlenecks or dependency delays.

📌Printer and Network-related incidents recorded the highest SLA breach rates at approximately 20.7%, slightly above other categories.

📌Anjali Mehta maintained the lowest SLA breach rate at 18.63%, indicating strong SLA compliance performance.

📌Categories with higher average resolution times also tended to exhibit higher SLA breach rates, suggesting a direct relationship between ticket complexity and SLA compliance performance.

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

