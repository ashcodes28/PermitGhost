from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from datetime import datetime


class Permit(Base):
    __tablename__ = "permits"

    id = Column(Integer, primary_key=True, index=True)
    permit_type = Column(String, nullable=False)
    zone = Column(String, nullable=False)
    status = Column(String, default="Active")
    risk_level = Column(String, default="Low")
    created_at = Column(DateTime, default=datetime.utcnow)


class Sensor(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, index=True)
    zone = Column(String, nullable=False)
    gas = Column(Float)
    temperature = Column(Float)
    pressure = Column(Float)
    updated_at = Column(DateTime, default=datetime.utcnow)


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    severity = Column(String)
    zone = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)