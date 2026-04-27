import pandas as pd
from sqlalchemy import create_engine, text
from transform import transform

# update with your postgres credentials
DB_URL = "postgresql+psycopg2://postgres:password@localhost:5432/olist"

def get_engine():
    return create_engine(DB_URL)

def load_to_db(df):
    """Push transformed DataFrame to PostgreSQL."""
    engine = get_engine()
    print("loading to postgres...")
    df.to_sql('orders_enriched', engine, if_exists='replace', index=False, chunksize=1000)
    print(f"loaded {len(df)} rows into orders_enriched")

    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM orders_enriched"))
        print("row count:", result.fetchone()[0])


if __name__ == "__main__":
    df = transform()
    load_to_db(df)
