from datetime import datetime
from typing import Optional, TypedDict

class CategoryDict(TypedDict, total=False):
    id: str
    name: str
    description: str
    created_at: str
    updated_at: str
    user_id: str
    is_global: bool
    parent_category_id: str
    
class Category:
    def __init__(
        self,
        id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        user_id: Optional[str] = None,
        is_global: Optional[bool] = None,
        parent_category_id: Optional[str] = None,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.user_id = user_id
        self.is_global = is_global
        self.parent_category_id = parent_category_id
        
    @classmethod
    def from_dict(cls, data: CategoryDict):
        """Crea una instancia de Category a partir de un diccionario."""
        try:
            return cls(
                id=data.get("id"),
                name=data["name"],
                description=data["description"],
                created_at=datetime.fromisoformat(data["created_at"])
                if "created_at" in data
                else None,
                updated_at=datetime.fromisoformat(data["updated_at"])
                if "updated_at" in data
                else None,
                user_id=data.get("user_id"),
                is_global=data.get("is_global"),
                parent_category_id=data.get("parent_category_id"),
            )
        except KeyError as e:
            raise ValueError(f"Missing required field: {e}")
        
    def to_dict(self) -> CategoryDict:
        """Convierte la instancia de Category a un diccionario."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "user_id": self.user_id,
            "is_global": self.is_global,
            "parent_category_id": self.parent_category_id,
        }