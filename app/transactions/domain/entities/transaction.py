from datetime import datetime
from typing import Optional, TypedDict
from enum import Enum

from app.transactions.domain.entities.categories import Category

class TransactionTypes(Enum):
    DEPOSIT = 'deposit'
    WITHDRAW = 'withdraw'
    TRANSFER = 'transfer'
    EARNS_INTEREST = 'earns_interest'
    
class TransactionDict(TypedDict, total = False):
    id: str
    user_id: str
    note: str
    description: str
    type: str
    transaction_date: str
    category_id: str
    category: Category
    created_at: str
    updated_at: str


class Transaction:
    category: Category = None
    
    def __init__(
        self,
        id: Optional[str] = None,
        user_id: Optional[str] = None,
        note: Optional[str] = None,
        description: Optional[str] = None,
        type: Optional[str] = None,
        transaction_date: Optional[datetime] = None,
        category_id: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.id = id
        self.user_id = user_id
        self.note = note
        self.description = description
        self.type = type
        self.transaction_date = (
            transaction_date or datetime.now()
        )
        self.category_id = category_id
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        

    @classmethod
    def from_dict(cls, data: TransactionDict):
        """Crea una instancia de Transaction a partir de un diccionario."""
        try:
            instance = cls(
                id=data.get("id"),
                user_id=data["user_id"],
                note=data["note"],
                description=data["description"],
                type=data["type"],
                transaction_date=datetime.fromisoformat(data["transaction_date"])
                if "transaction_date" in data
                else None,
                category_id=data["category_id"],
                created_at=datetime.fromisoformat(data["created_at"])
                if "created_at" in data
                else None,
                updated_at=datetime.fromisoformat(data["updated_at"])
                if "updated_at" in data
                else None,
            )
            instance.category = Category.from_dict(data["category"]) if data["category"] else None
            return instance
        except KeyError as e:
            raise ValueError(f"Missing required field: {e}")
          
    def to_dict(self) -> TransactionDict:
        """Convierte la instancia de Transaction a un diccionario."""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "note": self.note,
            "description": self.description,
            "type": self.type,
            "transaction_date": self.transaction_date.isoformat(),
            "category_id": self.category_id,
            "category": self.category.to_dict() if self.category else None,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }