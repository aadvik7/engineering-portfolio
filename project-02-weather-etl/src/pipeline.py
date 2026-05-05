import sys
import os
import schedule
import time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.extract import fetch_weather
from src.transform import transform_all
from src.load import insert_records
from config import CITIES, FETCH_INTERVAL


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
    print("pipeline done")


if __name__ == "__main__":
    run_pipeline()  # run once on start

    schedule.every(FETCH_INTERVAL).minutes.do(run_pipeline)
    print(f"scheduler running, fetching every {FETCH_INTERVAL} mins")

    while True:
        schedule.run_pending()
        time.sleep(30)
