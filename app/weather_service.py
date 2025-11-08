import requests
from app.config import OPENWEATHER_API_KEY, BASE_URL

def get_current_weather(location: str):
    if not OPENWEATHER_API_KEY:
        return {"error": "API key not set. Please check .env file."}

    # detect if input is numeric (pincode)
    if location.isdigit():
        params = {"zip": f"{location},in", "appid": OPENWEATHER_API_KEY, "units": "metric"}
    else:
        params = {"q": location, "appid": OPENWEATHER_API_KEY, "units": "metric"}

    try:
        resp = requests.get(BASE_URL, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.RequestException as e:
        return {"error": "Failed to fetch data", "details": str(e)}

    if "main" not in data or "weather" not in data:
        return {"error": "Invalid response", "details": data}

    return {
        "location": f"{data['name']}, {data['sys']['country']}",
        "current": {
            "temperature": round(data["main"]["temp"]),
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"].capitalize(),
        },
    }
