# app/models.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SensorData(BaseModel):
    gas_level: float
    smoke_level: float
    temperature: float
    timestamp: Optional[datetime] = None

# class Alert(BaseModel):
#     message: str
#     level: str  # example: "warning", "critical"
#     timestamp: Optional[datetime] = None
