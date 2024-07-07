SELECT * FROM [dbo].[SuperstoreSales]

SELECT Quantity, Profit 
FROM [dbo].[SuperstoreSales]
WHERE Quantity IS NULL

-- Total Revenue--
SELECT SUM(Sales) AS Total_Revenue
FROM SuperstoreSales

-- Average Order Value--
SELECT SUM(Sales)/ COUNT(DISTINCT(Order_ID)) AS Avg_Order_Sales
FROM SuperstoreSales

-- Total Quantity Sold--
SELECT SUM(Quantity) AS Quantity_Sold
FROM SuperstoreSales

-- Total Orders---
SELECT COUNT(DISTINCT Order_ID) AS Total_Orders
FROM SuperstoreSales

--DAILY TREND--
SELECT DATENAME(DW, Order_Date) AS order_day, COUNT(DISTINCT Order_ID) AS total_orders 
FROM SuperstoreSales
GROUP BY DATENAME(DW, Order_Date)


-- MONTHLY TREND--
SELECT DATENAME(MONTH, Order_Date) AS order_day, COUNT(DISTINCT Order_ID) AS total_orders 
FROM SuperstoreSales
GROUP BY DATENAME(MONTH, Order_Date)

-- YEARLY TREND--
SELECT DATENAME(YEAR, Order_Date) AS order_day, COUNT(DISTINCT Order_ID) AS total_orders 
FROM SuperstoreSales
GROUP BY DATENAME(YEAR, Order_Date)

--% OF sales by Category-- 
SELECT Category, CAST(SUM(Sales) AS DECIMAL(10,2)) as total_revenue,
CAST(SUM(Sales) * 100 / (SELECT SUM(Sales) from SuperstoreSales) AS DECIMAL(10,2)) AS PCT
FROM SuperstoreSales
GROUP BY Category

--TOP 5 Revenue by Sub_Category
SELECT TOP 5 Sub_Category, CAST(SUM(Sales)AS DECIMAL(10,2)) AS Revenue
FROM SuperstoreSales
GROUP BY Sub_Category
ORDER BY Revenue DESC

-- TOP 5 Quantity sold by Sub_Category--
SELECT DISTINCT TOP 5 Sub_Category, SUM(Quantity) AS Quantity_Sold
FROM SuperstoreSales
GROUP BY Sub_Category
ORDER BY Quantity_Sold DESC

-- BOTTOM 5 BY QUANTITY--
SELECT DISTINCT TOP  5 Sub_Category, SUM(Quantity) AS Quantity_Sold
FROM SuperstoreSales
GROUP BY Sub_Category
ORDER BY Quantity_Sold ASC


SELECT DISTINCT Customer_Name
FROM SuperstoreSales

--- TOP 5 Customers by Quantity ordered
SELECT DISTINCT TOP  5 Customer_Name, SUM(Quantity) AS Quantity_Sold
FROM SuperstoreSales
GROUP BY Customer_Name
ORDER BY Quantity_Sold DESC


--QUANTITY SOLD BY SEGMENT---
SELECT  Segment, SUM(Quantity) AS Quantity_Sold
FROM SuperstoreSales
GROUP BY Segment
ORDER BY Quantity_Sold DESC



--- Quantity Sold BY Segment---
SELECT  Region, SUM(Quantity) AS Quantity_Sold
FROM SuperstoreSales
GROUP BY Region
ORDER BY Quantity_Sold DESC