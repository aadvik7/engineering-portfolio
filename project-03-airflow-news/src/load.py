import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_URL = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

def get_engine():
    return create_engine(DB_URL)

def insert_articles(articles):
    """Insert articles into postgres, skip duplicates by url."""
    engine = get_engine()
    df = pd.DataFrame(articles)

    # dedup - skip urls already in db
    with engine.connect() as conn:
        existing = pd.read_sql("SELECT url FROM articles", conn)

    existing_urls = existing['url'].tolist()
    df = df[~df['url'].isin(existing_urls)]

    if df.empty:
        print("no new articles to insert")
        return

    df.to_sql('articles', engine, if_exists='append', index=False)
    print(f"inserted {len(df)} articles")
