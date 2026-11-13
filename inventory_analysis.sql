create database project;
select * from pharma_inventory;

SELECT 
Distribution_Hub,
Medicine_Name,
Current_Stock,
Expiry_Date,
CASE 
	WHEN DATEDIFF(Expiry_Date, CURRENT_DATE()) <= 90 THEN 'Dead-Stock Risk'
	ELSE 'Optimal' 
END AS Expiry_Risk_Status,
SUM(CASE WHEN Current_Stock = 0 THEN 1 ELSE 0 END) OVER(PARTITION BY Distribution_Hub) AS Hub_Stockout_Count
FROM pharma_inventory;