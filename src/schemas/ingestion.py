from pydantic import BaseModel, field_validator
from typing import List, Optional
from datetime import datetime

class LogEntry(BaseModel):
    timestamp: datetime
    caller_service: str
    target_url: str
    method: str
    status_code: int
    latency_ms: Optional[float] = None

    @field_validator('method')
    @classmethod
    def validate_method(cls, v):
        return v.upper()

class LogIngestionRequest(BaseModel):
    logs: List[LogEntry]

    @field_validator('logs')
    @classmethod
    def validate_logs(cls, v):
        if len(v) == 0:
            raise ValueError('Must provide at least one log entry')
        if len(v) > 10000:
            raise ValueError('Maximum 10,000 log entries per request')
        return v

class LogIngestionResponse(BaseModel):
    status: str
    processed_count: int
    dependencies_created: int
    dependencies_updated: int
    errors: List[str] = []