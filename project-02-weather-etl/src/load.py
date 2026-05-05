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
    # TODO: add dedup logic
    df.to_sql('weather_readings', engine, if_exists='append', index=False)
    print(f"inserted {len(df)} records")


if __name__ == "__main__":
    print("run pipeline.py to load data")
