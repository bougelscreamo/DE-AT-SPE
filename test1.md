# 1
SELECT u.user_id, u.name, SUM(o.amount) total_spending FROM orders o
JOIN users u ON u.user_id = o.user_id
GROUP BY u.user_id, u.name;


# 2
SELECT u.city, SUM(o.amount) AS city_spending FROM users u
JOIN orders o ON u.user_id = o.user_id
GROUP BY u.city
ORDER BY city_spending DESC
LIMIT 1;

# 3
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_users_city ON users(city);
