SELECT
  substr(order_date, 1, 7) AS month,
  ROUND(SUM(revenue), 2) AS total_revenue,
  COUNT(*) AS orders
FROM orders
GROUP BY substr(order_date, 1, 7)
ORDER BY month;
