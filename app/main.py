from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse
import json
from app.weather_service import get_current_weather

app = FastAPI(title="Current Weather API")

@app.get("/")
def home():
    return {"message": "Use /weather?location=city_name to get current weather"}

@app.get("/weather", response_class=PlainTextResponse)
def weather(location: str = Query(..., description="City name")):
    data = get_current_weather(location)
    
    formatted_output = json.dumps(data, indent=4)
    return PlainTextResponse(content=formatted_output, media_type="application/json")
