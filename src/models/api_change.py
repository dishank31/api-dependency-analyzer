from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from src.utils.db import Base

class ApiChange(Base):
    __tablename__ = "api_changes"
    
    id = Column(Integer, primary_key=True, index=True)
    endpoint_id = Column(Integer, ForeignKey("endpoints.id"), nullable=False, index=True)
    old_contract = Column(JSONB)
    new_contract = Column(JSONB)
    breaking_changes = Column(JSONB)
    impact_summary = Column(JSONB)
    analyzed_at = Column(DateTime(timezone=True), server_default=func.now())
    analyzed_by = Column(Integer, ForeignKey("users.id"))