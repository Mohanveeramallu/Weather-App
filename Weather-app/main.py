from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

# 3. Add the CORS middleware helper to our app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def home():
    return {"message": "Welcome to my Weather API server!"}

# Our new dynamic weather endpoint
@app.get("/api/weather")
def get_weather(lat: float, lon: float):
    # 1. Construct the Open-Meteo URL dynamically using the parameters passed by the user
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"
    
    # 2. Make the request to the third-party API (Your original logic)
    response = requests.get(url)
    data = response.json()
    
    # 3. Extract the temperature and wind speed
    temp = data["current"]["temperature_2m"]
    wind = data["current"]["wind_speed_10m"]
    
    # 4. Return a clean, custom JSON package to our frontend
    return {
        "latitude": lat,
        "longitude": lon,
        "temperature": temp,
        "wind_speed": wind,
        "unit": "degree centigrade"
    }