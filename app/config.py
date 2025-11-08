import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Optional debug check
if not OPENWEATHER_API_KEY:
    raise ValueError("Missing OpenWeather API key! Please set it in the .env file.")
