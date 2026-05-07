import schedule
import time
import logging
from extract import fetch_weather
from transform import transform_all
from load import insert_records
from config import CITIES

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def run():
    logging.info("fetching weather data...")
    results = []
    for city in CITIES:
        data = fetch_weather(city)
        if data:
            results.append((city, data))
        else:
            logging.warning(f"skipping {city}, no data")

    if not results:
        logging.warning("no data fetched, exiting")
        return

    records = transform_all(results)
    logging.info(f"got {len(records)} records")
    for r in records:
        logging.info(f"  {r['city']}: {r['temp']}°C, {r['weather_desc']}")
    insert_records(records)
    logging.info("done")


if __name__ == "__main__":
    logging.info("starting weather pipeline, runs every 60 min")
    schedule.every(60).minutes.do(run)
    run()
    while True:
        schedule.run_pending()
        time.sleep(60)
