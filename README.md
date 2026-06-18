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

