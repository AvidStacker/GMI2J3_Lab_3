from services.file_service import FileService
from services.weather_service import WeatherService

class App:
    def __init__(self, file_service, weather_service):
        self.file_service = file_service
        self.weather_service = weather_service

    def run(self, filepath, city):
        file_data = self.file_service.read_file(filepath)
        weather = self.weather_service.get_weather(city)
        return f"{file_data.strip()} | Weather: {weather['temp']}°C"
