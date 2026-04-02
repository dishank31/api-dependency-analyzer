from pydantic import BaseModel, field_validator
from typing import Optional, Dict, Any
from datetime import datetime

class EndpointCreate(BaseModel):
    path: str
    method: str
    contract_schema: Optional[Dict[str, Any]] = None

    @field_validator('method')
    @classmethod
    def validate_method(cls, v):
        allowed = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
        v = v.upper()
        if v not in allowed:
            raise ValueError(f'Method must be one of: {allowed}')
        return v

    @field_validator('path')
    @classmethod
    def validate_path(cls, v):
        if not v.startswith('/'):
            raise ValueError('Path must start with /')
        return v

class EndpointResponse(BaseModel):
    id: int
    service_id: int
    path: str
    method: str
    contract_schema: Optional[Dict[str, Any]]
    version: int
    created_at: datetime

    class Config:
        from_attributes = True