from pydantic import BaseModel, Field,EmailStr
from typing import Optional, List
from decimal import Decimal
import datetime
from sqlalchemy import Column, BigInteger, String, LargeBinary, TIMESTAMP, func
from database import Base
from models import *
class PropertyImage(Base):
    __tablename__ = "property_images"

    id = Column(BigInteger, primary_key=True, index=True)
    property_id = Column(BigInteger, index=True)
    image_url = Column(String(500), nullable=True)
    image_data = Column(LargeBinary, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

class PropertyCreate(BaseModel):
    title: str
    property_type: Optional[str] = None
    city: str
    project_name: Optional[str] = None
    possession_status: Optional[str] = None
    property_post_status: Optional[str] = None
    expected_price: Optional[Decimal] = None
    booking_amount: Optional[Decimal] = None
    is_price_negotiable: Optional[bool] = False
    carpet_area: Optional[Decimal] = None
    super_area: Optional[Decimal] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    balconies: Optional[int] = None
    rera_id: Optional[str] = None
    builder_name: Optional[str] = None
    builder_logo: Optional[str] = None
    nearby_landmarks: Optional[str] = None
    latitude: Optional[Decimal] = None
    longitude: Optional[Decimal] = None
    map_address: Optional[str] = None
    property_features: Optional[List[str]] = None
    facilities: Optional[List[str]] = None
    property_age: Optional[int] = None
    floor_number: Optional[int] = None
    total_floors: Optional[int] = None
    facing: Optional[str] = None
    furnished_status: Optional[str] = None
    parking_spaces: Optional[int] = None
    image_ids: Optional[List[int]] = []


class PropertyResponse(BaseModel):
    title: str
    property_type: Optional[str] = None
    city: str
    project_name: Optional[str] = None
    possession_status: Optional[str] = None
    property_post_status: Optional[str] = None
    expected_price: Optional[Decimal] = None
    booking_amount: Optional[Decimal] = None
    is_price_negotiable: Optional[bool] = False
    carpet_area: Optional[Decimal] = None
    super_area: Optional[Decimal] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    balconies: Optional[int] = None
    rera_id: Optional[str] = None
    builder_name: Optional[str] = None
    builder_logo: Optional[str] = None
    nearby_landmarks: Optional[str] = None
    latitude: Optional[Decimal] = None
    longitude: Optional[Decimal] = None
    map_address: Optional[str] = None
    property_features: Optional[List[str]] = None
    facilities: Optional[List[str]] = None
    property_age: Optional[int] = None
    floor_number: Optional[int] = None
    total_floors: Optional[int] = None
    facing: Optional[str] = None
    furnished_status: Optional[str] = None
    parking_spaces: Optional[int] = None
    image_ids: List[int] = Field(default_factory=list)


class ImageDownloadRequest(BaseModel):
    image_ids: List[int]

    class Config:
        from_attributes = True

class CustomerCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    password: str
    city: str | None = None


class AgentCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    password: str
    rera_number: str | None = None
    agency_name: str | None = None
    city: str | None = None


class BuilderCreate(BaseModel):
    company_name: str
    contact_person: str | None = None
    email: EmailStr
    phone: str
    password: str
    rera_number: str | None = None
    city: str | None = None

