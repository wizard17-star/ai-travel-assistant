import requests
import os
from dotenv import load_dotenv

load_dotenv()  

def get_weather_forecast(city: str) -> str:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "Weather API key is missing."

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return f"Could not fetch weather data for {city}."

    data = response.json()
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]

    return f"The weather in {city} is {description} with a temperature of {temp}°C."
