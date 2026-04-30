import requests
from config import CITIES

API_KEY = "abc123replacethis"

def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    print(f"\n--- {city} ---")
    print(data)
    return data


if __name__ == "__main__":
    for city in CITIES:
        fetch_weather(city)
