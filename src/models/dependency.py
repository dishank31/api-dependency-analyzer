from sqlalchemy import Column, Integer, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.utils.db import Base

class Dependency(Base):
    __tablename__ = "dependencies"
    
    id = Column(Integer, primary_key=True, index=True)
    caller_service_id = Column(Integer, ForeignKey("services.id"), nullable=False, index=True)
    callee_endpoint_id = Column(Integer, ForeignKey("endpoints.id"), nullable=False, index=True)
    call_frequency = Column(Integer, default=1)
    last_seen = Column(DateTime(timezone=True), server_default=func.now())
    first_seen = Column(DateTime(timezone=True), server_default=func.now())
    
    __table_args__ = (
        UniqueConstraint('caller_service_id', 'callee_endpoint_id', name='uq_dependency'),
    )
    
    caller_service = relationship(
        "Service",
        back_populates="outgoing_dependencies",
        foreign_keys=[caller_service_id]
    )
    callee_endpoint = relationship(
        "Endpoint",
        back_populates="incoming_dependencies",
        foreign_keys=[callee_endpoint_id]
    )
    
    def __repr__(self):
        return f"<Dependency(caller={self.caller_service_id}, callee_endpoint={self.callee_endpoint_id})>"