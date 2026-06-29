# Product Recommendation & Sales Analysis Dashboard

## Project Overview
This project analyzes retail sales data and builds a product recommendation system using Python, SQL, and Power BI.

The goal is to identify sales trends, customer behavior, and frequently bought product combinations to generate product recommendations.

---

## Tools & Technologies
- Python (Pandas, Matplotlib)
- MySQL
- Power BI

---

## Dataset Columns
- Order ID
- Order Date
- Customer Name
- Segment
- Region
- Product Name
- Category
- Sales
- Quantity
- Profit

---

## Project Workflow

### 1. Data Cleaning
- Handled missing values
- Removed duplicates
- Converted date columns

### 2. Exploratory Data Analysis
- Top selling products
- Most profitable products
- Sales by category
- Top customers
- Sales trends

### 3. Product Recommendation System
Built using SQL self-join logic to identify products frequently bought together.

### SQL Logic:
```sql
SELECT 
    a.`Product Name` AS Product_A,
    b.`Product Name` AS Product_B,
    COUNT(*) AS Frequency
FROM orders a
JOIN orders b 
ON a.`Order ID` = b.`Order ID`
AND a.`Product Name` < b.`Product Name`
GROUP BY a.`Product Name`, b.`Product Name`
ORDER BY Frequency DESC;
```

### Dashboard
<img width="489" height="759" alt="Screenshot 2026-04-24 154249" src="https://github.com/user-attachments/assets/491b9557-5b4a-4e2c-97a8-86ea83a01cdf" />


<img width="765" height="731" alt="Screenshot 2026-04-24 163426" src="https://github.com/user-attachments/assets/9618a9d9-e6d9-4394-8433-d69734d78dc7" />


<img width="765" height="484" alt="Screenshot 2026-04-24 163439" src="https://github.com/user-attachments/assets/1dd88a59-1988-44f0-a726-b76152349e5e" />





