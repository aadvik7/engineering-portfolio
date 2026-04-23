-- analytical queries for olist ecommerce data
-- running these against orders_enriched table


-- 1. monthly revenue trend
SELECT
    DATE_TRUNC('month', order_purchase_timestamp) AS month,
    ROUND(SUM(order_total)::numeric, 2) AS total_revenue,
    COUNT(DISTINCT order_id) AS num_orders
FROM orders_enriched
WHERE order_status = 'delivered'
GROUP BY 1
ORDER BY 1;


-- 2. top 10 product categories by revenue
SELECT
    product_category_name_english AS category,
    ROUND(SUM(order_total)::numeric, 2) AS total_revenue,
    COUNT(DISTINCT order_id) AS num_orders
FROM orders_enriched
WHERE order_status = 'delivered'
    AND product_category_name_english != 'unknown'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;


-- 3. average delivery time by state
SELECT
    customer_state,
    ROUND(AVG(delivery_days), 1) AS avg_delivery_days,
    COUNT(DISTINCT order_id) AS num_orders
FROM orders_enriched
WHERE order_status = 'delivered'
    AND delivery_days IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC;


-- 4. order volume by day of week
SELECT
    purchase_dow AS day_of_week,
    COUNT(DISTINCT order_id) AS num_orders,
    ROUND(SUM(order_total)::numeric, 2) AS total_revenue
FROM orders_enriched
WHERE order_status = 'delivered'
GROUP BY 1
ORDER BY 2 DESC;


-- 5. top sellers by revenue
SELECT
    seller_id,
    seller_state,
    ROUND(SUM(order_total)::numeric, 2) AS total_revenue,
    COUNT(DISTINCT order_id) AS num_orders
FROM orders_enriched
WHERE order_status = 'delivered'
GROUP BY 1, 2
ORDER BY 3 DESC
LIMIT 10;
