import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os

DB_URL = "postgresql+psycopg2://postgres:password@localhost:5432/olist"
OUTPUT_DIR = "output/charts/"  # charts saved here, gitignored

def get_engine():
    """Create SQLAlchemy engine using DB_URL."""
    return create_engine(DB_URL)

def run_query(engine, sql):
    """Run a SQL query and return results as a DataFrame."""
    return pd.read_sql(sql, engine)

def main():
    engine = get_engine()
    print("connected to db")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # monthly revenue
    q1 = """
        SELECT DATE_TRUNC('month', order_purchase_timestamp) AS month,
               ROUND(SUM(order_total)::numeric, 2) AS total_revenue
        FROM orders_enriched
        WHERE order_status = 'delivered'
        GROUP BY 1 ORDER BY 1
    """
    monthly = run_query(engine, q1)
    monthly['month'] = pd.to_datetime(monthly['month'])

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

    # chart 1 - monthly revenue trend
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(monthly['month'], monthly['total_revenue'], marker='o', color='steelblue')
    ax.set_title('Monthly Revenue Trend')
    ax.set_xlabel('Month')
    ax.set_ylabel('Revenue (BRL)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR + 'monthly_revenue.png')
    plt.close()
    print("saved monthly_revenue.png")

    # chart 2 - top 10 categories
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_cats['category'], top_cats['total_revenue'], color='coral')
    ax.set_title('Top 10 Product Categories by Revenue')
    ax.set_xlabel('Revenue (BRL)')
    ax.invert_yaxis()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR + 'top_categories.png')
    plt.close()
    print("saved top_categories.png")

    # chart 3 - avg delivery time by state
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.barh(delivery['customer_state'], delivery['avg_delivery_days'], color='mediumseagreen')
    ax.set_title('Avg Delivery Time by State (days)')
    ax.set_xlabel('Days')
    ax.invert_yaxis()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR + 'delivery_by_state.png')
    plt.close()
    print("saved delivery_by_state.png")

    # chart 4 - orders by day of week
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dow['day_of_week'] = pd.Categorical(dow['day_of_week'], categories=day_order, ordered=True)
    dow = dow.sort_values('day_of_week')

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(dow['day_of_week'], dow['num_orders'], color='mediumpurple')
    ax.set_title('Order Volume by Day of Week')
    ax.set_xlabel('Day')
    ax.set_ylabel('Number of Orders')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR + 'orders_by_dow.png')
    plt.close()
    print("saved orders_by_dow.png")

    print("all charts saved to", OUTPUT_DIR)


if __name__ == "__main__":
    main()
