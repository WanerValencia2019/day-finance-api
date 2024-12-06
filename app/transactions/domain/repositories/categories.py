
from abc import abstractmethod
from typing import List
from app.common.domain.repository import Repository
from app.transactions.domain.entities.categories import Category


class CategoriesRepository(Repository[Category]):
  pass