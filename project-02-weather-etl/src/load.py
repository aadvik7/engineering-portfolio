import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_URL = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

def get_engine():
    return create_engine(DB_URL)

def insert_records(records):
    """Insert weather records, skip duplicates."""
    engine = get_engine()
    df = pd.DataFrame(records)

    # dedup - don't insert if same city + timestamp already exists
    with engine.connect() as conn:
        existing = pd.read_sql(
            "SELECT city, fetched_at FROM weather_readings", conn
        )

    if not existing.empty:
        existing_pairs = set(zip(existing['city'], existing['fetched_at'].astype(str)))
        df = df[~df.apply(lambda r: (r['city'], str(r['fetched_at'])) in existing_pairs, axis=1)]

    if df.empty:
        print("no new records to insert")
        return

    df.to_sql('weather_readings', engine, if_exists='append', index=False)
    print(f"inserted {len(df)} records")


if __name__ == "__main__":
    print("run pipeline.py to load data")
