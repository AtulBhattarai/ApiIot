# app/crud.py

from .database import sensor_data_collection
from .models import SensorData
from datetime import datetime
from bson import ObjectId

def insert_sensor_data(data: SensorData):
    # Convert data to dictionary
    record = data.dict()
    record["timestamp"] = datetime.utcnow()

    # Insert into MongoDB
    result = sensor_data_collection.insert_one(record)

    # Prepare the response
    response = {
        "id": str(result.inserted_id),
        "temperature": record["temperature"],
        "humidity": record["humidity"],
        "mq2": record["mq2"],
        "mq135": record["mq135"],
        "fire": record["fire"],
        "timestamp": record["timestamp"]
    }
    return response

def get_10_recent_sensor_data(limit: int = 10):
    # Fetch records, sort by latest timestamp
    records = sensor_data_collection.find().sort("timestamp", -1).limit(limit)

    # Convert cursor to list and clean ObjectId
    result = []
    for record in records:
        record["_id"] = str(record["_id"])  # Convert ObjectId to string
        result.append(record)

    return result


def get_latest_sensor_data(limit: int = 1):
    # Fetch records, sort by latest timestamp
    records = sensor_data_collection.find().sort("timestamp", -1).limit(limit)

    # Convert cursor to list and clean ObjectId
    result = []
    for record in records:
        record["_id"] = str(record["_id"])  # Convert ObjectId to string
        result.append(record)

    return result

