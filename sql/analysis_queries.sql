-- ═══════════════════════════════════════════════
-- IT HELPDESK ANALYTICS — SQL ANALYSIS QUERIES
-- DATABASE: it_helpdesk
-- TABLE: tickets
-- ═══════════════════════════════════════════════

USE it_helpdesk;

-- ─────────────────────────────────────────
-- SECTION 1 — BASIC EXPLORATION
-- ─────────────────────────────────────────

-- Q1: Total number of tickets
SELECT COUNT(*) AS total_tickets
FROM tickets;

-- Q2: How many tickets per status?
SELECT 
    status,
    COUNT(*) AS total_tickets,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS percentage
FROM tickets
GROUP BY status
ORDER BY total_tickets DESC;

-- Q3: How many tickets per priority?
SELECT 
    priority,
    COUNT(*) AS total_tickets,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS percentage
FROM tickets
GROUP BY priority
ORDER BY total_tickets DESC;

-- Q4: How many tickets per category?
SELECT 
    category,
    COUNT(*) AS total_tickets,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS percentage
FROM tickets
GROUP BY category
ORDER BY total_tickets DESC;

-- Q5: How many tickets per department?
SELECT 
    department,
    COUNT(*) AS total_tickets
FROM tickets
GROUP BY department
ORDER BY total_tickets DESC;


-- ─────────────────────────────────────────
-- SECTION 2 — SLA ANALYSIS
-- ─────────────────────────────────────────

-- Q6: Overall SLA breach rate
SELECT
    sla_breached,
    COUNT(*) AS total,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS percentage
FROM tickets
GROUP BY sla_breached;

-- Q7: SLA breach rate by priority
SELECT
    priority,
    COUNT(*) AS total_tickets,
    SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) AS breached,
    ROUND(SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) 
          * 100.0 / COUNT(*), 2) AS breach_rate_percent
FROM tickets
WHERE sla_breached != 'Pending'
GROUP BY priority
ORDER BY breach_rate_percent DESC;

-- Q8: SLA breach rate by category
SELECT
    category,
    COUNT(*) AS total_tickets,
    SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) AS breached,
    ROUND(SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) 
          * 100.0 / COUNT(*), 2) AS breach_rate_percent
FROM tickets
WHERE sla_breached != 'Pending'
GROUP BY category
ORDER BY breach_rate_percent DESC;

-- Q9: SLA breach rate by department
SELECT
    department,
    COUNT(*) AS total_tickets,
    SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) AS breached,
    ROUND(SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) 
          * 100.0 / COUNT(*), 2) AS breach_rate_percent
FROM tickets
WHERE sla_breached != 'Pending'
GROUP BY department
ORDER BY breach_rate_percent DESC;

-- Q10: Do weekend tickets breach SLA more than weekday tickets?
SELECT
    is_weekend,
    COUNT(*) AS total_tickets,
    SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) AS breached,
    ROUND(SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) 
          * 100.0 / COUNT(*), 2) AS breach_rate_percent
FROM tickets
WHERE sla_breached != 'Pending'
GROUP BY is_weekend;


-- ─────────────────────────────────────────
-- SECTION 3 — AGENT PERFORMANCE
-- ─────────────────────────────────────────

-- Q11: Total tickets handled per agent
SELECT
    assigned_agent,
    COUNT(*) AS total_tickets
FROM tickets
GROUP BY assigned_agent
ORDER BY total_tickets DESC;

-- Q12: Average resolution time per agent
SELECT
    assigned_agent,
    ROUND(AVG(resolution_hours), 2) AS avg_resolution_hours,
    MIN(resolution_hours)           AS fastest_resolution,
    MAX(resolution_hours)           AS slowest_resolution
FROM tickets
WHERE resolution_hours IS NOT NULL
GROUP BY assigned_agent
ORDER BY avg_resolution_hours ASC;

-- Q13: SLA breach rate per agent (agent performance leaderboard)
SELECT
    assigned_agent,
    COUNT(*) AS total_tickets,
    SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) AS breached,
    ROUND(SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) 
          * 100.0 / COUNT(*), 2) AS breach_rate_percent,
    ROUND(AVG(resolution_hours), 2) AS avg_resolution_hours
FROM tickets
WHERE sla_breached != 'Pending'
GROUP BY assigned_agent
ORDER BY breach_rate_percent ASC;  -- best performers first


-- ─────────────────────────────────────────
-- SECTION 4 — TREND ANALYSIS
-- ─────────────────────────────────────────

-- Q14: Monthly ticket volume trend
SELECT
    created_year,
    created_month,
    created_month_name,
    COUNT(*) AS total_tickets
FROM tickets
GROUP BY created_year, created_month, created_month_name
ORDER BY created_year, created_month;

-- Q15: Which day of week gets most tickets?
SELECT
    created_day,
    COUNT(*) AS total_tickets
FROM tickets
GROUP BY created_day
ORDER BY total_tickets DESC;

-- Q16: Which hour of day gets most tickets? (peak hours)
SELECT
    created_hour,
    COUNT(*) AS total_tickets
FROM tickets
GROUP BY created_hour
ORDER BY created_hour;

-- Q17: Monthly SLA breach trend
SELECT
    created_year,
    created_month_name,
    COUNT(*) AS total_tickets,
    SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) AS breached,
    ROUND(SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) 
          * 100.0 / COUNT(*), 2) AS breach_rate_percent
FROM tickets
WHERE sla_breached != 'Pending'
GROUP BY created_year, created_month, created_month_name
ORDER BY created_year, created_month;


-- ─────────────────────────────────────────
-- SECTION 5 — ADVANCED QUERIES
-- ─────────────────────────────────────────

-- Q18: Resolution bucket distribution
SELECT
    resolution_bucket,
    COUNT(*) AS total_tickets,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS percentage
FROM tickets
GROUP BY resolution_bucket
ORDER BY total_tickets DESC;

-- Q19: Critical tickets that breached SLA (highest business risk)
SELECT
    ticket_id,
    category,
    department,
    assigned_agent,
    created_date,
    resolved_date,
    resolution_hours
FROM tickets
WHERE priority   = 'Critical'
AND   sla_breached = 'Yes'
ORDER BY resolution_hours DESC
LIMIT 20;

-- Q20: Department + Category combination with most SLA breaches
SELECT
    department,
    category,
    COUNT(*) AS total_tickets,
    SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) AS breached,
    ROUND(SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) 
          * 100.0 / COUNT(*), 2) AS breach_rate_percent
FROM tickets
WHERE sla_breached != 'Pending'
GROUP BY department, category
ORDER BY breach_rate_percent DESC
LIMIT 10;


-- ─────────────────────────────────────────
-- SECTION 6 — VIEWS FOR POWER BI
-- ─────────────────────────────────────────
-- Views are saved queries — Power BI will connect to these

-- View 1: Agent performance summary
CREATE OR REPLACE VIEW vw_agent_performance AS
SELECT
    assigned_agent,
    COUNT(*) AS total_tickets,
    ROUND(AVG(resolution_hours), 2) AS avg_resolution_hours,
    SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) AS total_breaches,
    ROUND(SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) 
          * 100.0 / COUNT(*), 2) AS breach_rate_percent
FROM tickets
WHERE sla_breached != 'Pending'
GROUP BY assigned_agent;

-- View 2: Monthly trend summary
CREATE OR REPLACE VIEW vw_monthly_trend AS
SELECT
    created_year,
    created_month,
    created_month_name,
    COUNT(*) AS total_tickets,
    SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) AS breached_tickets,
    ROUND(AVG(resolution_hours), 2) AS avg_resolution_hours
FROM tickets
GROUP BY created_year, created_month, created_month_name
ORDER BY created_year, created_month;

-- View 3: Category SLA summary
CREATE OR REPLACE VIEW vw_category_sla AS
SELECT
    category,
    priority,
    COUNT(*) AS total_tickets,
    ROUND(AVG(resolution_hours), 2) AS avg_resolution_hours,
    SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) AS breached,
    ROUND(SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) 
          * 100.0 / COUNT(*), 2) AS breach_rate_percent
FROM tickets
WHERE sla_breached != 'Pending'
GROUP BY category, priority;

-- Confirm views created
SHOW FULL TABLES WHERE Table_type = 'VIEW';