# Stock News Service

from utils.api_requests import fetch_data
import config

def get_headline_data():
    params = {
        "apiKey": config.HEADLINES_API_KEY,
        "country": config.HEADLINES_COUNTRY,
        "category": config.HEADLINES_CATEGORY
    }
    
    data = fetch_data(config.HEADLINES_URL, params=params)
    
    if data:
        return data["articles"][0:3]
    else:
        return None