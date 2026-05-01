SELECT Supplier, AVG(Delay_Days) AS avg_delay
FROM clean_supply_chain
GROUP BY Supplier
ORDER BY avg_delay DESC;

SELECT Region, AVG(Delay_Days) AS avg_delay
FROM clean_supply_chain
GROUP BY Region
ORDER BY avg_delay DESC;

SELECT Delivery_Status, COUNT(*) AS total_orders
FROM clean_supply_chain
GROUP BY Delivery_Status;
