
-- Match low movement items in DC1 with same items in DC2 that have acceptable movement
SELECT dc2.ITEM, dc1.Total_Use AS 'DC1 Use', dc2.Total_Use AS 'DC2 Use'
FROM dc1UsageData dc1
JOIN dc2UsageData dc2
ON dc1.ITEM = dc2.ITEM
WHERE dc1.Total_Use < 50 AND dc2.Total_Use > 50

-- Do the same from DC2 to DC1
SELECT dc2.ITEM, dc1.Total_Use AS 'DC1 Use', dc2.Total_Use AS 'DC2 Use'
FROM dc1UsageData dc1
JOIN dc2UsageData dc2
ON dc1.ITEM = dc2.ITEM
WHERE dc1.Total_Use > 50 AND dc2.Total_Use < 50

--Most profitable items
SELECT 
	ITEM, 
	Item_Category, 
	Total_Use, 
	(Total_Use * Unit_Cost) AS 'Total Cost', 
	(Total_Use * Avg_Sell) AS 'Total Revenue', 
	((Total_Use * Avg_Sell) - (Total_Use * Unit_Cost)) AS 'Total Profit'
FROM dc1UsageData
ORDER BY 'Total Profit' desc

--Least profitable items
SELECT 
	ITEM, 
	Item_Category, 
	Total_Use, 
	(Total_Use * Unit_Cost) AS 'Total Cost', 
	(Total_Use * Avg_Sell) AS 'Total Revenue', 
	((Total_Use * Avg_Sell) - (Total_Use * Unit_Cost)) AS 'Total Profit'
FROM dc1UsageData
ORDER BY 'Total Profit' desc 

-- Profitability of item categories
SELECT 
	Item_Category, 
	SUM(Total_Use) AS 'Total Use', 
	SUM(Total_Use * Unit_Cost) AS 'Total Cost', 
	SUM(Total_Use * Avg_Sell) AS 'Total Revenue', 
	SUM((Total_Use * Avg_Sell) - (Total_Use * Unit_Cost)) AS 'Total Profit'
FROM dc1UsageData
GROUP BY Item_Category
ORDER BY 'Total Profit'

-- Compare between DCs
SELECT 
	dc1.Item_Category, 
	SUM(dc1.Total_Use) AS 'DC1 Total Use',
	SUM(dc2.Total_Use) AS 'DC2 Total Use',
	SUM(dc1.Total_Use * dc1.Unit_Cost) AS 'DC1 Total Cost',
	SUM(dc2.Total_Use * dc2.Unit_Cost) AS 'DC2 Total Cost',
	SUM(dc1.Total_Use * dc1.Avg_Sell) AS 'DC1 Total Revenue',
	SUM(dc2.Total_Use * dc2.Avg_Sell) AS 'DC2 Total Revenue', 
	SUM((dc1.Total_Use * dc1.Avg_Sell) - (dc1.Total_Use * dc1.Unit_Cost)) AS 'DC1 Total Profit',
	SUM((dc2.Total_Use * dc2.Avg_Sell) - (dc2.Total_Use * dc2.Unit_Cost)) AS 'DC2 Total Profit'
FROM dc1UsageData dc1
JOIN dc2UsageData dc2
ON dc1.ITEM = dc2.ITEM
GROUP BY dc1.Item_Category
ORDER BY 'DC1 Total Profit'

-- Calculate differences between DCs
WITH Comparison AS (
SELECT 
	dc1.Item_Category, 
	SUM(dc1.Total_Use) AS 'DC1 Total Use',
	SUM(dc2.Total_Use) AS 'DC2 Total Use',
	SUM(dc1.Total_Use * dc1.Unit_Cost) AS 'DC1 Total Cost',
	SUM(dc2.Total_Use * dc2.Unit_Cost) AS 'DC2 Total Cost',
	SUM(dc1.Total_Use * dc1.Avg_Sell) AS 'DC1 Total Revenue',
	SUM(dc2.Total_Use * dc2.Avg_Sell) AS 'DC2 Total Revenue', 
	SUM((dc1.Total_Use * dc1.Avg_Sell) - (dc1.Total_Use * dc1.Unit_Cost)) AS 'DC1 Total Profit',
	SUM((dc2.Total_Use * dc2.Avg_Sell) - (dc2.Total_Use * dc2.Unit_Cost)) AS 'DC2 Total Profit'
FROM dc1UsageData dc1
JOIN dc2UsageData dc2
ON dc1.ITEM = dc2.ITEM
GROUP BY dc1.Item_Category
)
SELECT 
	Item_Category,
	[DC2 Total Use] - [DC1 Total Use] AS 'Use Difference DC2 over DC1',
	[DC2 Total Cost] - [DC1 Total Cost] AS 'Cost Difference DC2 over DC1',
	[DC2 Total Revenue] - [DC1 Total Revenue] AS 'Revenue Difference DC2 over DC1',
	[DC2 Total Profit] - [DC1 Total Profit] AS 'Profit Difference DC2 over DC1' 
FROM Comparison
ORDER BY 'Profit Difference DC2 over DC1' desc
