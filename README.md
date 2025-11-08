🌦️ FastAPI Weather App

A simple FastAPI project that provides current weather details for any city name or pincode, using the OpenWeather API.

🚀 Features

Get current temperature, humidity, and weather condition
Supports both city name and pincode
Clean JSON response
Built with FastAPI

▶️ Run the Application
uvicorn app.main:app --reload

Now open your browser:

Home Page → http://127.0.0.1:8000
Weather Example → http://127.0.0.1:8000/weather?location=bangalore

📋 Example Output
{
    "location": "Bengaluru, IN",
    "current": {
        "temperature": 28,
        "humidity": 60,
        "condition": "Clear sky"
    }
}
