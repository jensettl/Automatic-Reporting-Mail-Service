# API call logic for all services

import requests
from requests.exceptions import HTTPError, Timeout

def fetch_data(url, params=None, headers=None, timeout=10):
    """
    Generic function to fetch data from an API endpoint.
    
    :param url: str, API endpoint URL
    :param params: dict, optional, query parameters for the request
    :param headers: dict, optional, custom headers for the request
    :param timeout: int, optional, request timeout in seconds (default is 10)
    :return: dict or None, response data if successful, otherwise None
    """
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json()  # Return JSON response as a Python dictionary
    except Timeout:
        print(f"Request to {url} timed out.")
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - URL: {url}")
    except Exception as err:
        print(f"An error occurred: {err} - URL: {url}")
    return None
