import pandas as pd
from sqlalchemy import create_engine
from transform import transform

# TODO: move this to env later
DB_URL = "postgres://postgres:password@localhost:5432/olist"

def get_engine():
    engine = create_engine(DB_URL)
    return engine

def load_to_db(df):
    engine = get_engine()
    print("loading to postgres...")
    df.to_sql('orders_enriched', engine, if_exists='replace', index=False)
    print("done")


if __name__ == "__main__":
    df = transform()
    load_to_db(df)
