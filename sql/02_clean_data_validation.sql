SELECT COUNT(*) AS total_rows FROM clean_supply_chain;

SELECT COUNT(*) AS null_check
FROM clean_supply_chain
WHERE Order_Date IS NULL OR Delivery_Date IS NULL;

SELECT MIN(Cost), MAX(Cost)
FROM clean_supply_chain;
