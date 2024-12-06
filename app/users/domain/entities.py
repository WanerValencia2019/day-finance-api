from datetime import datetime, timezone
from typing import Optional, TypedDict


class UserDict(TypedDict, total=False):
    id: str
    name: str
    email: str
    password: str
    created_at: str
    updated_at: str


class User:
    def __init__(
        self,
        id: Optional[str] = None,
        name: Optional[str] = None,
        email: Optional[str] = None,
        password: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.created_at = (
            created_at or datetime.utcnow()
        )  # Usa el tiempo actual si no se especifica.
        self.updated_at = updated_at or datetime.utcnow()

    @classmethod
    def from_dict(cls, data: UserDict):
        """Crea una instancia de User a partir de un diccionario."""
        try:
            return cls(
                id=data.get("id"),
                name=data["name"],
                email=data["email"],
                password=data["password"],
                created_at=datetime.fromisoformat(data["created_at"])
                if "created_at" in data
                else None,
                updated_at=datetime.fromisoformat(data["updated_at"])
                if "updated_at" in data
                else None,
            )
        except KeyError as e:
            raise ValueError(f"Missing required field: {e}")

    def to_dict(self) -> UserDict:
        """Convierte la instancia de User a un diccionario."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
