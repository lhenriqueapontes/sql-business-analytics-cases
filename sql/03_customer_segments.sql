SELECT
  c.segment,
  c.region,
  COUNT(DISTINCT c.customer_id) AS customers,
  COUNT(o.order_id) AS orders,
  ROUND(SUM(o.revenue), 2) AS total_revenue,
  ROUND(AVG(o.revenue), 2) AS avg_order_value
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.segment, c.region
ORDER BY total_revenue DESC;
