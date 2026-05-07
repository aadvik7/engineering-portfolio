import requests
import os
import logging
from dotenv import load_dotenv
from config import CITIES

load_dotenv()
API_KEY = os.getenv('OWM_API_KEY')

def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"error fetching {city}: {e}")
        return None


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    for city in CITIES:
        print(fetch_weather(city))
