from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.utils.db import Base

class Endpoint(Base):
    __tablename__ = "endpoints"
    
    id = Column(Integer, primary_key=True, index=True)
    service_id = Column(Integer, ForeignKey("services.id", ondelete="CASCADE"), nullable=False, index=True)
    path = Column(String(500), nullable=False)
    method = Column(String(10), nullable=False)
    contract_schema = Column(JSONB)
    version = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    __table_args__ = (
        UniqueConstraint('service_id', 'path', 'method', name='uq_service_endpoint'),
    )
    
    service = relationship("Service", back_populates="endpoints")
    incoming_dependencies = relationship(
        "Dependency",
        back_populates="callee_endpoint",
        foreign_keys="Dependency.callee_endpoint_id"
    )
    
    def __repr__(self):
        return f"<Endpoint(id={self.id}, {self.method} {self.path})>"