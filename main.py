# Entry point of your application

from services.weather_service import get_weather_data, get_astronomy_data
from services.stocks_service import get_stock_info

from utils.data_cleaner import clean_weather_data, clean_astronomy_data, clean_stock_data
from utils.email_builder import build_email_body, sendEmail

import config

TODAY = config.TODAY
TICKER_LIST = config.TICKER_LIST

def main():
    # Fetch data 
    weather_data = get_weather_data(config.QUERY)
    astronomy_data = get_astronomy_data(config.QUERY, TODAY)
    stock_data = get_stock_info(TICKER_LIST)
    
    # Clean and structure data
    cleaned_weather = clean_weather_data(weather_data)
    cleaned_astronomy = clean_astronomy_data(astronomy_data)
    cleaned_stock = clean_stock_data(stock_data)
    
    # Build email body
    email_body = build_email_body(cleaned_weather, cleaned_astronomy, cleaned_stock)
    
    # Send email
    sendEmail(config.EMAIL_FROM, config.EMAIL_TO, "Daily Report", email_body)
    
if __name__ == "__main__":
    main()