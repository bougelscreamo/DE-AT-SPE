# Total sales by Product Category per day
SELECT
  d.date,
  p.category,
  SUM(f.total_amount) AS total_sales
FROM fact_sales f
JOIN dim_date d ON f.date_id = d.date_id
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY d.date, p.category;


# Total sales by region per month
SELECT
  d.year,
  d.month,
  c.region,
  SUM(f.total_amount) AS total_sales
FROM fact_sales f
JOIN dim_date d ON f.date_id = d.date_id
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY d.year, d.month, c.region;
