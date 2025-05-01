# app/main.py

from fastapi import FastAPI, HTTPException
from .models import SensorData
from . import crud
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for mobile app/frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Smart Kitchen Disaster Prevention API!"}

# Endpoint to submit sensor data
@app.post("/sensor-data/")
def submit_sensor_data(data: SensorData):
    saved_data = crud.insert_sensor_data(data)
    return {"status": "success", "data": saved_data}

# Endpoint to get recent sensor data
@app.get("/sensor-data/")
def get_sensor_data():
    data = crud.get_10_recent_sensor_data()
    print(data)
    return {"status": "success", "data": data}

# Endpoint to get latest sensor data
@app.get("/latest-sensor-data/")
def get_latest_sensor_data():
    data = crud.get_latest_sensor_data()
    print(data)
    return {"status": "success", "data": data}
