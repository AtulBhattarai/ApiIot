# app/crud.py

from .database import sensor_data_collection
from .models import SensorData
from datetime import datetime
from bson import ObjectId

# Insert sensor data
# def insert_sensor_data(data: SensorData):
#     record = data.dict()

#     record["timestamp"] = datetime.utcnow()
#     print(record)
#     sensor_data_collection.insert_one(record)
#     return record

def insert_sensor_data(data: SensorData):
    # Convert data to dictionary
    record = data.dict()
    record["timestamp"] = datetime.utcnow()

    # Insert into MongoDB
    result = sensor_data_collection.insert_one(record)

    # Prepare the response
    response = {
        "id": str(result.inserted_id),
        "gas_level": record["gas_level"],
        "smoke_level": record["smoke_level"],
        "temperature": record["temperature"],
        "timestamp": record["timestamp"]
    }
    return response

# Get recent sensor data
# def get_recent_sensor_data(limit: int = 10):
#     # records = sensor_data_collection.find().sort("timestamp", -1).limit(limit)
#     records = sensor_data_collection.find()
#     print(records)

#     return records



def get_recent_sensor_data(limit: int = 10):
    # Fetch records, sort by latest timestamp
    records = sensor_data_collection.find().sort("timestamp", -1).limit(limit)

    # Convert cursor to list and clean ObjectId
    result = []
    for record in records:
        record["_id"] = str(record["_id"])  # Convert ObjectId to string
        result.append(record)

    return result


# # Insert an alert
# def insert_alert(alert: Alert):
#     record = alert.dict()
#     record["timestamp"] = datetime.utcnow()
#     alerts_collection.insert_one(record)
#     return record

# # Get recent alerts
# def get_recent_alerts(limit: int = 10):
#     records = alerts_collection.find().sort("timestamp", -1).limit(limit)
#     return list(records)
