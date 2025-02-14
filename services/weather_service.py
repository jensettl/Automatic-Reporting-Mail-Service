# Logic for fetching and handling weather data

from utils.api_requests import fetch_data
import config

def get_weather_data(query: str):
    """
    Fetch weather data from the WeatherAPI.
    
    :return: dict or None, weather data if successful, otherwise None
    """
    
    url = config.WEATHER_URL
    params = {
        "key": config.WEATHER_API_KEY,
        "q": config.QUERY,
    }
    weather_data = fetch_data(url, params=params)
    
    if weather_data:
        return weather_data
    else:
        print(f"Failed to fetch weather data for {query}.")
        return None
      

def get_astronomy_data(query: str, date: str):
    """
    Fetch astronomy data from the WeatherAPI.
    
    :return: dict or None, astronomy data if successful, otherwise None
    """
    
    url = config.ASTRONOMY_URL
    params = {
        "key": config.WEATHER_API_KEY,
        "q": config.QUERY,
        "dt": config.TODAY,
    }
    astronomy_data = fetch_data(url, params=params)
    
    if astronomy_data:
        return astronomy_data
    else:
        print(f"Failed to fetch astronomy data for {query} on {date}.")
        return None