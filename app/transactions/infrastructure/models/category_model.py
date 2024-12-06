from uuid import uuid4
from sqlalchemy import UUID, Boolean, Column, ForeignKey, String

from app.core.database.postgresql.connection import Base
        
class CategoryAlchemyModel(Base):
    __tablename__ = 'categories'
  
    id = Column(UUID(as_uuid=True),default=uuid4(), primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    parent_category_id = Column(UUID(as_uuid=True), ForeignKey('categories.id'), nullable=True)
    is_global = Column(Boolean, default=False, index=True)
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)
    
    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name}, description={self.description}, user_id={self.user_id}, parent_category_id={self.parent_category_id}, created_at={self.created_at}, updated_at={self.updated_at})>"
  