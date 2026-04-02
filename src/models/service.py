from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.utils.db import Base

class Service(Base):
    __tablename__ = "services"
    
    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(1000))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    __table_args__ = (
        UniqueConstraint('team_id', 'name', name='uq_team_service_name'),
    )
    
    team = relationship("Team", back_populates="services")
    endpoints = relationship("Endpoint", back_populates="service", cascade="all, delete-orphan")
    outgoing_dependencies = relationship(
        "Dependency",
        back_populates="caller_service",
        foreign_keys="Dependency.caller_service_id"
    )
    
    def __repr__(self):
        return f"<Service(id={self.id}, name={self.name})>"
    