
-- QUERY 1: DAILY MIS REPORT

SELECT
    purchase_date,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(payment_total), 2) AS revenue,
    ROUND(AVG(payment_total), 2) AS avg_order_value
FROM orders_mis
GROUP BY purchase_date
ORDER BY purchase_date;


-- QUERY 2: WEEKLY MIS REPORT

SELECT
    week_start,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(payment_total), 2) AS revenue,
    ROUND(AVG(review_score), 2) AS avg_review
FROM orders_mis
GROUP BY week_start
ORDER BY week_start;


-- QUERY 3: MONTHLY REVENUE REPORT

SELECT
    year_month,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(payment_total), 2) AS total_revenue,
    ROUND(AVG(payment_total), 2) AS average_order_value
FROM orders_mis
GROUP BY year_month
ORDER BY year_month;


-- QUERY 4: OPERATIONAL PERFORMANCE REPORT

SELECT
    order_status,
    COUNT(*) AS total_orders,
    ROUND(AVG(delivery_days), 2) AS avg_delivery_days,
    ROUND(AVG(review_score), 2) AS avg_review_score
FROM orders_mis
GROUP BY order_status;


-- QUERY 5: SELLER PERFORMANCE

SELECT
    seller_id,
    SUM(unique_orders) AS total_orders,
    SUM(total_items) AS total_items,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM seller_mis
GROUP BY seller_id
ORDER BY total_revenue DESC
LIMIT 10;


-- QUERY 6: CATEGORY PERFORMANCE

SELECT
    category,
    SUM(total_items) AS total_items,
    SUM(unique_orders) AS total_orders,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM category_mis
GROUP BY category
ORDER BY total_revenue DESC
LIMIT 10;


-- QUERY 7: DATA AUDIT REPORT

SELECT
    "Check",
    "Count"
FROM data_audit
ORDER BY "Count" DESC;


-- QUERY 8: DELAYED DELIVERY ANALYSIS

SELECT
    order_id,
    purchase_date,
    delivery_days,
    delay_days,
    review_score
FROM orders_mis
WHERE order_status = 'delivered'
  AND delay_days > 0
ORDER BY delay_days DESC;


-- QUERY 9: MONTH-OVER-MONTH REVENUE COMPARISON

WITH monthly AS (
    SELECT
        year_month,
        SUM(payment_total) AS revenue
    FROM orders_mis
    GROUP BY year_month
),

comparison AS (
    SELECT
        year_month,
        revenue,
        LAG(revenue) OVER (
            ORDER BY year_month
        ) AS previous_revenue
    FROM monthly
)

SELECT
    year_month,
    ROUND(revenue, 2) AS current_revenue,
    ROUND(previous_revenue, 2) AS previous_revenue,
    ROUND(
        100.0 * (revenue - previous_revenue)
        / NULLIF(previous_revenue, 0),
        2
    ) AS growth_percentage
FROM comparison
ORDER BY year_month;


-- QUERY 10: CUSTOMER REVIEW MONITORING

SELECT
    review_score,
    COUNT(*) AS total_reviews
FROM orders_mis
WHERE review_score IS NOT NULL
GROUP BY review_score
ORDER BY review_score;
