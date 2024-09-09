import requests

class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, city):
        url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={city}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["current"]["temperature"]
        else:
            raise Exception("Failed to fetch weather data")
