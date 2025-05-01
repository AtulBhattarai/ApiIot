# app/database.py

from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from a .env file if you have
load_dotenv()

# MongoDB connection string
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Create/Get database
db = client.smart_kitchen_db

# Create/Get collections
sensor_data_collection = db.sensor_data
# alerts_collection = db.alerts
