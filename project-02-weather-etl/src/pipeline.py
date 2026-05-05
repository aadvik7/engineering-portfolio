import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.extract import fetch_weather
from src.transform import transform_all
from src.load import insert_records
from config import CITIES


def run_pipeline():
    print("running pipeline...")

    raw_data = []
    for city in CITIES:
        raw = fetch_weather(city)
        print(f"got data for {city}")
        raw_data.append((city, raw))

    records = transform_all(raw_data)
    print(f"transformed {len(records)} records")

    insert_records(records)


if __name__ == "__main__":
    run_pipeline()
