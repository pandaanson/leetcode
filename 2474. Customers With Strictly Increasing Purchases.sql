WITH YearlyData AS (
    SELECT 
        customer_id, 
        YEAR(order_date) AS order_year, 
        LAG(YEAR(order_date)) OVER (PARTITION BY customer_id ORDER BY YEAR(order_date)) AS prev_year,
        RANK() OVER (PARTITION BY customer_id ORDER BY YEAR(order_date)) AS rank_by_year,
        RANK() OVER (PARTITION BY customer_id ORDER BY SUM(price)) AS rank_by_price
    FROM Orders
    GROUP BY customer_id, YEAR(order_date)
)
SELECT DISTINCT customer_id
FROM YearlyData
WHERE customer_id NOT IN (
    SELECT customer_id 
    FROM YearlyData 
    WHERE prev_year IS NOT NULL AND ((order_year - prev_year) != 1 OR rank_by_year != rank_by_price)
);
