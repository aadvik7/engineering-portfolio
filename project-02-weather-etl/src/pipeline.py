import schedule
import time
from extract import fetch_weather
from transform import transform_all
from load import insert_records
from config import CITIES

def run():
    print("fetching weather data...")
    results = [(city, fetch_weather(city)) for city in CITIES]
    records = transform_all(results)
    print(f"got {len(records)} records")
    for r in records:
        print(f"  {r['city']}: {r['temp']}°C, {r['weather_desc']}")
    insert_records(records)
    print("done")


if __name__ == "__main__":
    print("starting weather pipeline, runs every 60 min")
    schedule.every(60).minutes.do(run)
    run()  # run once immediately on start
    while True:
        schedule.run_pending()
        time.sleep(60)
