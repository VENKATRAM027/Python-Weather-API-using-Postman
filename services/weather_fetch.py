

import os
import requests

def fetch_weather_for_city(city_name):
    """
    Fetches live weather data from the OpenWeatherMap API.
    """
    # 1. Get your secret API key from the .env file
    api_key = os.getenv("WEATHER_API_KEY")
    
    if not api_key or api_key == "paste_your_real_api_key_here":
        print("Configuration Error: Missing valid WEATHER_API_KEY in .env file.")
        return None

    # 2. Construct the URL for the OpenWeatherMap API
    # We use units=metric to get Celsius instead of Kelvin
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    try:
        # 3. Make the HTTP GET request to the external service
        response = requests.get(url)
        
        # 4. Check if the external API found the city (Status 200 OK)
        if response.status_code == 200:
            # Parse the JSON response from OpenWeather
            data = response.json()
            
            # Extract and format only the specific data we want to return to our users
            formatted_data = {
                "temperature": data['main']['temp'],
                "condition": data['weather'][0]['main'],
                "humidity": data['main']['humidity']
            }
            return formatted_data
            
        # 5. Handle the case where OpenWeather can't find the city
        elif response.status_code == 404:
            return None
            
        # Handle other potential errors (like exceeding your free API limits)
        else:
            print(f"External API Error: Received status code {response.status_code}")
            return None
            
    # Handle network errors (e.g., your internet is down)
    except requests.exceptions.RequestException as e:
        print(f"Network request failed: {e}")
        return None