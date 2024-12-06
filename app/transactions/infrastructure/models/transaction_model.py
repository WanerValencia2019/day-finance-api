from uuid import uuid4
from sqlalchemy import UUID, Column, DateTime, Float, ForeignKey, String, Enum
from app.core.database.postgresql.connection import Base
from sqlalchemy.orm import relationship, Mapped

from datetime import datetime

from app.transactions.domain.entities.transaction import TransactionTypes
from app.transactions.infrastructure.models.category_model import CategoryAlchemyModel

class TransactionAlchemyModel(Base):
    __tablename__ = 'transactions'

    id = Column(UUID(as_uuid=True),default=uuid4(), primary_key=True, index=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    note = Column(String, nullable=False)
    description = Column(String)
    type = Column(Enum(TransactionTypes), nullable=False)
    transaction_date = Column(DateTime, nullable=False)
    category_id = Column(UUID(as_uuid=True), ForeignKey('categories.id'), nullable=False)
    category: Mapped[CategoryAlchemyModel] = relationship(CategoryAlchemyModel)
    amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    
    def __repr__(self):
        return f"<Transaction(id={self.id}, user_id={self.user_id}, note={self.note}, description={self.description}, type={self.type}, transaction_date={self.transaction_date}, category_id={self.category_id}, amount={self.amount}, created_at={self.created_at}, updated_at={self.updated_at})>"