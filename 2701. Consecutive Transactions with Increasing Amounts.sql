-- MySQL query to find customers with increasing transactions over at least three consecutive days
WITH Consecutive_Increasing_Transactions AS (
    SELECT a.customer_id, a.transaction_date
    FROM Transactions a, Transactions b
    WHERE a.customer_id = b.customer_id 
      AND b.amount > a.amount
      AND DATEDIFF(b.transaction_date, a.transaction_date) = 1
),
Numbered_Transactions AS (
    SELECT 
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY transaction_date) AS row_num, 
        customer_id, 
        transaction_date
    FROM Consecutive_Increasing_Transactions
),
Base_Date_Assigned AS (
    SELECT 
        customer_id, 
        transaction_date,
        DATE_SUB(transaction_date, INTERVAL row_num DAY) AS base_date
    FROM Numbered_Transactions
),
Grouped_Transactions AS (
    SELECT 
        customer_id, 
        MIN(transaction_date) AS earliest_transaction, 
        COUNT(*) AS consecutive_count
    FROM Base_Date_Assigned
    GROUP BY customer_id, base_date
)
SELECT 
    customer_id, 
    earliest_transaction AS consecutive_start,
    DATE_ADD(earliest_transaction, INTERVAL consecutive_count DAY) AS consecutive_end
FROM Grouped_Transactions
WHERE consecutive_count >= 2
ORDER BY customer_id;
