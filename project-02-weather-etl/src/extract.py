import requests
from config import CITIES

API_KEY = "abc123replacethis"

def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    # print specific fields to understand structure
    print(f"\n--- {city} ---")
    print("temp:", data['main']['temp'])
    print("feels_like:", data['main']['feels_like'])
    print("humidity:", data['main']['humidity'])
    print("weather:", data['weather'][0]['description'])
    print("wind speed:", data['wind']['speed'])

    return data


if __name__ == "__main__":
    for city in CITIES:
        fetch_weather(city)
