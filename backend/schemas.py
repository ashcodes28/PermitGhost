from pydantic import BaseModel
from datetime import datetime


# ---------- Permit ----------

class PermitCreate(BaseModel):
    permit_type: str
    zone: str


class PermitResponse(BaseModel):
    id: int
    permit_type: str
    zone: str
    status: str
    risk_level: str
    created_at: datetime

    class Config:
        from_attributes = True


# ---------- Sensor ----------

class SensorResponse(BaseModel):
    id: int

    zone: str

    temperature: float
    humidity: float
    pressure: float
    gas: float

    workers: int

    active_permit: str

    equipment_status: str

    event: str

    risk_level: str

    updated_at: datetime

    class Config:
        from_attributes = True


# ---------- Alert ----------

class AlertResponse(BaseModel):
    id: int
    title: str
    description: str
    severity: str
    zone: str
    created_at: datetime

    class Config:
        from_attributes = True