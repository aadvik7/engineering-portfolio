import requests

API_KEY = "abc123replacethis"

def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    print(response.status_code)
    print(response.json())
    return response.json()


if __name__ == "__main__":
    fetch_weather("Delhi")
