from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

_T = TypeVar('_T')

class Repository(ABC, Generic[_T]):
    @abstractmethod
    def find(self, id: str) -> Optional[_T]:
        pass

    @abstractmethod
    def find_all(self) -> List[_T]:
        pass

    @abstractmethod
    def save(self, entity: _T) -> None:
        pass

    @abstractmethod
    def update(self, entity: _T) -> None:
        pass
      
    @abstractmethod
    def delete(self, entity: _T) -> None:
        pass
      