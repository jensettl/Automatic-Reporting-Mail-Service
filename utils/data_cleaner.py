# Data cleaning and transformation functions

from datetime import datetime

def clean_weather_data(weather_data):
    """
    Clean and structure weather data from the API response.
    
    :param weather_data: dict, raw weather data from the weather API
    :return: dict, cleaned weather data with relevant information
    """
    if not weather_data or "location" not in weather_data:
        return None
    
    cleaned_data = {
        "location": weather_data["location"]["name"],
        "country": weather_data["location"]["country"],
        "temperature": weather_data["current"]["temp_c"],
        "humidity": weather_data["current"]["humidity"],
        "wind_speed": weather_data["current"]["wind_kph"],
        "condition": weather_data["current"]["condition"]["text"],
        "last_updated": parse_timestamp(weather_data["current"]["last_updated"])
    }
    return cleaned_data

def clean_astronomy_data(astronomy_data):
    """
    Clean and structure astronomy data from the API response.
    
    :param astronomy_data: dict, raw astronomy data from the weather API
    :return: dict, cleaned astronomy data with relevant information
    """
    
    if not astronomy_data or "location" not in astronomy_data:
        return None
    
    cleaned_data = {
        "sunrise": astronomy_data["astronomy"]["astro"]["sunrise"],
        "sunset": astronomy_data["astronomy"]["astro"]["sunset"],
        "moonrise": astronomy_data["astronomy"]["astro"]["moonrise"],
        "moonset": astronomy_data["astronomy"]["astro"]["moonset"]
    }
    
    return cleaned_data

def clean_stock_data(stock_data):
    """
    Clean and structure stock data from the API response.
    
    :param stock_data: dict, raw stock data from the stock API
    :return: dict, cleaned stock data with relevant information
    """
    if not stock_data:
        return None
    
    cleaned_data = stock_data   # for future data cleaning
    
    return cleaned_data

def clean_headlines_data(headlines_data):
    """
    Clean and structure headlines data from the API response.
    
    :param headlines_data: dict, raw headlines data from the news API
    :return: list, cleaned headlines data with relevant information
    """
    
    if not headlines_data:
        print("No articles found in the headlines data.")
        return None
    
    cleaned_data = []
    for article in headlines_data:
        cleaned_article = {
            "source": article["source"].get("name", "No source available"),
            "author": article["author"],
            "title": article["title"],
            "description": article["description"],
            "url": article["url"],
            "published_at": parse_timestamp(article["publishedAt"])
        }
        cleaned_data.append(cleaned_article)
    
    return cleaned_data
    

def parse_timestamp(timestamp_str):
    """
    Convert a timestamp string into a readable datetime format.
    
    :param timestamp_str: str, timestamp in the format 'YYYY-MM-DD HH:MM:SS'
    :return: str, formatted timestamp like 'Feb 9, 2025 at 10:30 AM'
    """
    try:
        dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        return dt.strftime("%b %d, %Y at %I:%M %p")
    except ValueError:
        return timestamp_str  # Return the original string if parsing fails
