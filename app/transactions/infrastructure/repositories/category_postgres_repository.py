from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.transactions.domain.entities.categories import Category
from app.transactions.domain.repositories.categories import CategoriesRepository
from app.transactions.infrastructure.models.category_model import CategoryAlchemyModel


class CategoriesPostgresRepository(CategoriesRepository):
  def __init__(self, session: AsyncSession):
    self.session = session
    
  async def find(self, id: str):
    result = await self.session.execute(
      select(CategoryAlchemyModel).where(CategoryAlchemyModel.id == id)
    )
    category_model = result.scalars().first()
    return self._to_entity(category_model) if category_model else None
  
  async def find_all(self):
    result = await self.session.execute(select(CategoryAlchemyModel))
    return [self._to_entity(category) for category in result.scalars().all()]
  
  async def create(self, category: Category):
    category_model = CategoryAlchemyModel(
      id=category.id, name=category.name, description=category.description
    )
    self.session.add(category_model)
    await self.session.commit()
    await self.session.refresh(category_model)
    return self._to_entity(category_model)
  
  
  async def update(self, category: Category):
    category_model = await self.session.get(CategoryAlchemyModel, category.id)
    if not category_model:
      raise ValueError(f"Category with id {category.id} not found ")
    
    category_model.name = category.name
    category_model.description = category.description
    await self.session.commit()
    await self.session.refresh(category_model)
    return self._to_entity(category_model)
  
  async def delete(self, id: str):
    category_model = await self.session.get(CategoryAlchemyModel, id)
    if not category_model:
      raise ValueError(f"Category with id {id} not found")
    await self.session.delete(category_model)
    await self.session.commit()
    
  def _to_entity(self, category_model: CategoryAlchemyModel) -> Category:
    return Category.from_dict(category_model.__dict__)
    