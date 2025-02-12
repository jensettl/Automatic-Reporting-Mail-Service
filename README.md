# Automatic Reporting Mail Service


## Project Overview

The `Automatic Reporting Mail Service` fetches weather, astronomy, and stock data from various `APIs`, processes the data, and sends a formatted email report to a specified email address. The service is designed to run automatically at a specified time each day on a `Raspberry Pi`.



## Dependencies

- Python 3.x
- `requests`
- `yfinance`

## Configuration

Edit the `config.py` file to include your API keys, email address, and Gmail password.

```python
from datetime import datetime

WEATHER_API_KEY = ""  # API key for Weather API (FreeWeatherAPI)[https://www.weatherapi.com/]
EMAIL_FROM = ""   # Email adress for sending emails
EMAIL_TO = ""   # Email adress for sending emails
EMAIL_PWD = ""     # Password set in Google account settings
SMTP_SERVER = "smtp.gmail.com"  # SMTP server for sending emails
SMTP_PORT = 587  # Standard port for email submission

TICKER_LIST = ["GOOGL", "AAPL", "MSFT", "AMZN", "TSLA", "NVDA"] # List of stock tickers to fetch data for
TODAY = datetime.now().strftime("%Y-%m-%d")  # Get today's date in format "YYYY-MM-DD"
QUERY = "Karlsruhe"  # City for which to fetch weather and astronomy data
```
