from pydantic import BaseModel
from sqlalchemy import TIMESTAMP, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text

from database import Base


class UserTable(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(
        String(30)
    )  # consider using ENUM if you have a finite set of genders
    phone = Column(String(50))  # phone is a string to keep leading zeros
    country = Column(String(100))
    created_at = Column(TIMESTAMP, server_default=text("(datetime('now'))"))
    updated_at = Column(TIMESTAMP, server_default=text("(datetime('now'))"))
    user_quality = relationship("UserQuality", back_populates="user")


class User(BaseModel):
    username: str
    name: str
    age: int
    gender: str
    phone: str
    country: str


class UserQuality(Base):
    __tablename__ = "users_quality"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    current_weight = Column(Float)
    height = Column(Float)
    waist_measurement = Column(Float)
    chest_measurement = Column(Float)
    hip_measurement = Column(Float)
    body_type = Column(
        String(100)
    )  # consider using ENUM if you have a finite set of body types
    measurement_date = Column(TIMESTAMP, server_default="datetime('now')")

    user = relationship("UserTable", back_populates="user_quality")


class UserQualityModel(BaseModel):
    user_id: int
    current_weight: float
    height: float
    waist_measurement: float
    chest_measurement: float
    hip_measurement: float
    body_type: str
    user: User
