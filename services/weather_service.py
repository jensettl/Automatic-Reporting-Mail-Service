# Logic for fetching and handling weather data

from utils.api_requests import fetch_data
import config

def get_weather_data(query: str):
    """
    Fetch weather data from the WeatherAPI.
    
    :return: dict or None, weather data if successful, otherwise None
    """
    
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": f"{config.WEATHER_API_KEY}",
        "q": f"{query}",
    }
    weather_data = fetch_data(url, params=params)
    
    if weather_data:
        return weather_data
    else:
        print(f"Failed to fetch weather data for {query}.")
        return None