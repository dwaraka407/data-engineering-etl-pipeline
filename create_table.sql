CREATE TABLE fact_sales (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product STRING,
    quantity INT,
    price FLOAT,
    total_price FLOAT,
    order_date DATE
);
