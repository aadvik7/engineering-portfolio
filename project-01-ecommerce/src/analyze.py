import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

DB_URL = "postgresql+psycopg2://postgres:password@localhost:5432/olist"

def get_engine():
    return create_engine(DB_URL)

def run_query(engine, sql):
    return pd.read_sql(sql, engine)

def main():
    engine = get_engine()
    print("connected to db")

    # monthly revenue
    q1 = """
        SELECT DATE_TRUNC('month', order_purchase_timestamp) AS month,
               ROUND(SUM(order_total)::numeric, 2) AS total_revenue
        FROM orders_enriched
        WHERE order_status = 'delivered'
        GROUP BY 1 ORDER BY 1
    """
    monthly = run_query(engine, q1)
    print("monthly revenue:")
    print(monthly.head())

    # top categories
    q2 = """
        SELECT product_category_name_english AS category,
               ROUND(SUM(order_total)::numeric, 2) AS total_revenue
        FROM orders_enriched
        WHERE order_status = 'delivered'
          AND product_category_name_english != 'unknown'
        GROUP BY 1 ORDER BY 2 DESC LIMIT 10
    """
    top_cats = run_query(engine, q2)
    print("top categories:")
    print(top_cats)

    # delivery by state
    q3 = """
        SELECT customer_state,
               ROUND(AVG(delivery_days), 1) AS avg_delivery_days
        FROM orders_enriched
        WHERE order_status = 'delivered' AND delivery_days IS NOT NULL
        GROUP BY 1 ORDER BY 2 DESC LIMIT 15
    """
    delivery = run_query(engine, q3)

    # orders by day of week
    q4 = """
        SELECT purchase_dow AS day_of_week,
               COUNT(DISTINCT order_id) AS num_orders
        FROM orders_enriched
        WHERE order_status = 'delivered'
        GROUP BY 1 ORDER BY 2 DESC
    """
    dow = run_query(engine, q4)

    return monthly, top_cats, delivery, dow


if __name__ == "__main__":
    main()
