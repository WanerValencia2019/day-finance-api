
from sqlalchemy import Column,DateTime, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.core.database.postgresql.connection import Base

from datetime import datetime
from uuid import uuid4

class UserAlchemyModel(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True),default=uuid4(), index=True, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, name={self.name}, is_active={self.is_active}, created_at={self.created_at}, updated_at={self.updated_at})>"
