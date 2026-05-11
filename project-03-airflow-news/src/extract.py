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
        'pageSize': 100,
        'apiKey': API_KEY
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"api error: {response.status_code}")
        return []

    data = response.json()
    articles = data.get('articles', [])
    print(f"got {len(articles)} articles")
    return articles


if __name__ == "__main__":
    articles = fetch_news()
    if articles:
        print(articles[0].get('title'))
