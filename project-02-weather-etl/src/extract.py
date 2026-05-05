import requests
import os
from dotenv import load_dotenv
from config import CITIES

load_dotenv()
API_KEY = os.getenv('OWM_API_KEY')

def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    for city in CITIES:
        print(f"\n--- {city} ---")
        print(fetch_weather(city))
