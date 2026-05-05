import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_URL = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

def get_engine():
    return create_engine(DB_URL)

def insert_records(records):
    """Insert a list of weather record dicts into postgres."""
    engine = get_engine()
    df = pd.DataFrame(records)

    # skip cities already recorded in the last hour
    with engine.connect() as conn:
        existing = pd.read_sql(
            "SELECT city FROM weather_readings WHERE fetched_at > NOW() - INTERVAL '1 hour'",
            conn
        )
    already_done = existing['city'].tolist()
    df = df[~df['city'].isin(already_done)]

    if df.empty:
        print("nothing new to insert")
        return

    df.to_sql('weather_readings', engine, if_exists='append', index=False)
    print(f"inserted {len(df)} records")


if __name__ == "__main__":
    print("run pipeline.py to load data")
