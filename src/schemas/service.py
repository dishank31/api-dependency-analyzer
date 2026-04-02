import re
from pydantic import BaseModel, field_validator
from typing import Optional, List
from datetime import datetime

class ServiceCreate(BaseModel):
    name: str
    description: Optional[str] = None

    @field_validator('name')
    @classmethod
    def name_format(cls, v):
        v = v.strip()
        if not v:
            raise ValueError('Service name cannot be empty')
        if len(v) > 255:
            raise ValueError('Service name too long (max 255 chars)')
        if not re.match(r'^[a-zA-Z0-9_-]+$', v):
            raise ValueError('Only letters, numbers, hyphens, underscores allowed')
        return v.lower()   # normalise: "Payment-Service" → "payment-service"

class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class ServiceResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    team_id: int
    created_at: datetime
    endpoint_count: Optional[int] = 0

    class Config:
        from_attributes = True

class ServiceListResponse(BaseModel):
    services: List[ServiceResponse]