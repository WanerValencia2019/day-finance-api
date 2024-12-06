from abc import ABC, abstractmethod
from typing import List

from app.transactions.domain.entities.transaction import Transaction


class TransactionRepository(ABC):
    @abstractmethod
    def get_transaction(self, transaction_id: str) -> Transaction:
        pass

    @abstractmethod
    def get_transactions(self) -> List[Transaction]:
        pass

    @abstractmethod
    def create_transaction(self, transaction: Transaction) -> Transaction:
        pass

    @abstractmethod
    def update_transaction(self, transaction: Transaction) -> Transaction:
        pass

    @abstractmethod
    def delete_transaction(self, transaction_id: str) -> None:
        pass