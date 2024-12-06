from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.transactions.domain.entities.transaction import Transaction
from app.transactions.domain.repositories.transaction import TransactionRepository

from app.transactions.infrastructure.models.transaction_model import TransactionAlchemyModel


class TransactionPostgresRepository(TransactionRepository):
  def __init__(self, session: AsyncSession):
    self.session = session  
    
  async def get_transaction(self, transaction_id: str) -> Transaction:
    result = await self.session.execute(
      select(TransactionAlchemyModel).where(TransactionAlchemyModel.id == transaction_id)
    )
    transaction_model = result.scalars().first()
    return self._to_entity(transaction_model) if transaction_model else None
  
  
  async def get_transactions(self) -> List[Transaction]:
    result = await self.session.execute(select(TransactionAlchemyModel))
    return [self._to_entity(transaction) for transaction in result.scalars().all()]
  
  async def create_transaction(self, transaction: Transaction) -> Transaction:
    transaction_model = TransactionAlchemyModel(
      id=transaction.id, user_id=transaction.user_id, note=transaction.note, description=transaction.description,
      type=transaction.type, transaction_date=transaction.transaction_date, category_id=transaction.category_id,
      amount=transaction.amount
    )
    self.session.add(transaction_model)
    await self.session.commit()
    await self.session.refresh(transaction_model)
    return self._to_entity(transaction_model)
  
  async def update_transaction(self, transaction: Transaction) -> Transaction:
    transaction_model = await self.session.get(TransactionAlchemyModel, transaction.id)
    if not transaction_model:
      raise ValueError(f"Transaction with id {transaction.id} not found")
    transaction_model.user_id = transaction.user_id
    transaction_model.note = transaction.note
    transaction_model.description = transaction.description
    transaction_model.type = transaction.type
    transaction_model.transaction_date = transaction.transaction_date
    transaction_model.category_id = transaction.category_id
    transaction_model.amount = transaction.amount
    await self.session.commit()
    await self.session.refresh(transaction_model)
    return self._to_entity(transaction_model)
  
  async def delete_transaction(self, transaction_id: str) -> None:
    transaction_model = await self.session.get(TransactionAlchemyModel, transaction_id)
    if not transaction_model:
      raise ValueError(f"Transaction with id {transaction_id} not found")
    await self.session.delete(transaction_model)
    await self.session.commit()
    
  def _to_entity(self, transaction_model: TransactionAlchemyModel) -> Transaction:
    return Transaction.from_dict(transaction_model.__dict__)