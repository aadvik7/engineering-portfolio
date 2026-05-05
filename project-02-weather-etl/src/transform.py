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
        'wind_gust': raw['wind'].get('gust'),      # not always in response
        'rain_1h': raw.get('rain', {}).get('1h'),  # optional
        'fetched_at': datetime.utcnow()
    }

def transform_all(results):
    """Parse a list of (city, raw_response) tuples."""
    return [parse_weather(raw, city) for city, raw in results]
