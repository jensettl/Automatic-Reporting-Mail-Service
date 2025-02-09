# Unit test for weather_service.py

import unittest
from services.weather_service import get_weather_data, get_astronomy_data

class TestWeatherService(unittest.TestCase):
    def test_get_weather_data_success(self):
        data = get_weather_data("Karlsruhe")
        self.assertIsNotNone(data)
        self.assertIn("location", data)
        
    def test_get_weather_data_failure(self):
        data = get_weather_data()
        self.assertIsNone(data)
        self.assertNotIn("location", data)
        
    def test_get_weather_data_invalid(self):
        data = get_weather_data("Invalid")
        self.assertIsNone(data)
        self.assertNotIn("location", data)
    
    def test_get_weather_data_empty(self):
        data = get_weather_data("")
        self.assertIsNone(data)
        self.assertNotIn("location", data)
        
    def test_get_weather_data_none(self):
        data = get_weather_data(None)
        self.assertIsNone(data)
        self.assertNotIn("location", data)
        
    def test_get_weather_data_number(self):
        data = get_weather_data(123)
        self.assertIsNone(data)
        self.assertNotIn("location", data)
        
    def test_get_weather_data_list(self):
        data = get_weather_data(["Karlsruhe"])
        self.assertIsNone(data)
        self.assertNotIn("location", data)
        
    def test_astromony_data(self):
        data = get_astronomy_data("Karlsruhe", date="2021-01-01")
        self.assertIsNotNone(data)
        self.assertIn("location", data)

if __name__ == "__main__":
    unittest.main()
