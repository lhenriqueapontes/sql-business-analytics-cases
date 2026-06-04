SELECT
  p.product_name,
  p.category,
  ROUND(SUM(o.revenue), 2) AS total_revenue,
  SUM(o.quantity) AS units_sold
FROM orders o
JOIN products p ON p.product_id = o.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY total_revenue DESC
LIMIT 10;
