import requests

class WeatherService:
    def get_weather(self, city):
        response = requests.get(f"http://fake-weather-api.com/{city}")
        return response.json()
