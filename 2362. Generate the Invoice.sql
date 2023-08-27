WITH InvoiceTotal AS (
  -- Step 1: Calculate the total price for each invoice
  SELECT p.invoice_id, SUM(pr.price * p.quantity) AS total_price
  FROM Purchases p
  JOIN Products pr ON p.product_id = pr.product_id
  GROUP BY p.invoice_id
),
MaxInvoice AS (
  -- Step 2: Identify the invoice with the highest total price
  SELECT invoice_id
  FROM InvoiceTotal
  ORDER BY total_price DESC, invoice_id ASC
  LIMIT 1
)
-- Step 3: List the details of the items in the selected invoice
SELECT p.product_id, p.quantity, (pr.price * p.quantity) AS price
FROM Purchases p
JOIN Products pr ON p.product_id = pr.product_id
WHERE p.invoice_id = (SELECT invoice_id FROM MaxInvoice)
