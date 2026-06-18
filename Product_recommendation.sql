use sales;
show tables;
select * from orders;

-- Top Selling Products
SELECT Product_name, SUM(Sales) AS Total_Sales
FROM orders
GROUP BY Product_name
ORDER BY Total_Sales DESC
LIMIT 10;

-- Most Profitable Products
SELECT Product_name, SUM(Profit) AS Total_Profit
FROM orders
GROUP BY Product_name
ORDER BY Total_Profit DESC
LIMIT 10;

-- Sales by Category
SELECT Category, SUM(Sales) AS Total_Sales
FROM orders
GROUP BY Category
ORDER BY Total_Sales DESC;

-- Top Customers
SELECT `Customer Name`, SUM(Sales) AS Total_Sales
FROM orders
GROUP BY `Customer Name`
ORDER BY Total_Sales DESC
LIMIT 10;

-- Top Products by Quantity
SELECT Product_name, SUM(Quantity) AS Total_Quantity
FROM orders
GROUP BY Product_name
ORDER BY Total_Quantity DESC
LIMIT 10;

-- Frequently Product Bought Togeth
SELECT 
    a.Product_name AS Product_A,
    b.Product_name AS Product_B,
    COUNT(*) AS Frequency
FROM orders a
JOIN orders b 
ON a.`Order ID` = b.`Order ID`
AND a.Product_name <> b.Product_name
GROUP BY Product_A, Product_B
ORDER BY Frequency DESC
LIMIT 10;



-- Recommendation for a Specific Product
SELECT 
    b.Product_name AS Recommended_Product,
    COUNT(*) AS Frequency
FROM orders a
JOIN orders b 
ON a.`Order ID` = b.`Order ID`
-- Change Product name from here
WHERE a.Product_name = 'Bush Somerset Collection Bookcase'
AND b.Product_name != a.Product_name
GROUP BY b.Product_name
ORDER BY Frequency DESC
LIMIT 5;

-- Category-Based Recommendation
SELECT Product_name, SUM(Sales) AS Total_Sales
FROM orders
WHERE Category = (
    SELECT Category
    FROM orders
    WHERE Product_name = 'Bush Somerset Collection Bookcase'
    LIMIT 1
)
GROUP BY Product_name
ORDER BY Total_Sales DESC
LIMIT 10;

