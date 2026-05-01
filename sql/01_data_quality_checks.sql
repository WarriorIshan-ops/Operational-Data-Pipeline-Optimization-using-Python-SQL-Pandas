SELECT COUNT(*) AS total_rows FROM supply_chain_raw;

SELECT COUNT(*) AS missing_dates
FROM supply_chain_raw
WHERE Order_Date IS NULL OR Delivery_Date IS NULL;

SELECT COUNT(*) AS invalid_cost
FROM supply_chain_raw
WHERE Cost IS NULL OR Cost < 0;
