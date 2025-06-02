import unittest
from unittest.mock import MagicMock
from app import App

class TestApp(unittest.TestCase):
    def test_run_with_mocks(self):
        mock_file_service = MagicMock()
        mock_weather_service = MagicMock()

        mock_file_service.read_file.return_value = "Hello from file"
        mock_weather_service.get_weather.return_value = {"temp": 22}

        app = App(mock_file_service, mock_weather_service)
        result = app.run("dummy.txt", "Gothenburg")

        self.assertEqual(result, "Hello from file | Weather: 22°C")

if __name__ == '__main__':
    unittest.main()
