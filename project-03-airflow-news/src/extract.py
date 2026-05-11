import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('NEWS_API_KEY')

def fetch_news(query="technology", language="en"):
    url = "https://newsapi.org/v2/everything"
    params = {
        'q': query,
        'language': language,
        'apiKey': API_KEY
    }
    response = requests.get(url, params=params)
    print(response.status_code)
    print(response.json())
    return response.json()


if __name__ == "__main__":
    fetch_news()
