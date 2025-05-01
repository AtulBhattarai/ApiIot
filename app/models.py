# app/models.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SensorData(BaseModel):
    temperature: str
    humidity: str
    mq2: str
    mq135: str
    fire: str 
    timestamp: Optional[datetime] = None
