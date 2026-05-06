from extract import fetch_weather
from transform import transform_all
from load import insert_records
from config import CITIES

def run():
    print("fetching weather data...")
    results = [(city, fetch_weather(city)) for city in CITIES]
    records = transform_all(results)
    insert_records(records)
    print("done")


if __name__ == "__main__":
    run()
