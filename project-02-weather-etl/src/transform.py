from datetime import datetime

def parse_weather(raw, city):
    return {
        'city': city,
        'temp': raw['main']['temp'],
        'feels_like': raw['main']['feels_like'],
        'humidity': raw['main']['humidity'],
        'pressure': raw['main']['pressure'],
        'weather_desc': raw['weather'][0]['description'],
        'wind_speed': raw['wind']['speed'],
        'fetched_at': datetime.utcnow()
    }
