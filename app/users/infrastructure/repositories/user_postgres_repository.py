from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from app.users.infrastructure.models.user_model import UserAlchemyModel
from app.users.domain.entities import User

from uuid import UUID
from typing import Optional, List


class PostgresUserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: User) -> User:
        user_model = UserAlchemyModel(
            id=user.id, name=user.name, email=user.email, password=user.password
        )
        self.session.add(user_model)
        await self.session.commit()
        await self.session.refresh(user_model)
        return self._to_entity(user_model)

    async def get_by_id(self, user_id: UUID) -> Optional[User]:
        result = await self.session.execute(
            select(UserAlchemyModel).where(UserAlchemyModel.id == user_id)
        )
        user_model = result.scalars().first()
        return self._to_entity(user_model) if user_model else None

    async def get_by_email(self, email: str) -> Optional[User]:
        result = await self.session.execute(
            select(UserAlchemyModel).where(UserAlchemyModel.email == email)
        )
        user_model = result.scalars().first()
        return self._to_entity(user_model) if user_model else None

    async def list(self) -> List[User]:
        result = await self.session.execute(select(UserAlchemyModel).options(joinedload("*")))
        return [self._to_entity(user) for user in result.scalars().all()]

    async def update(self, user: User) -> User:
        user_model = await self.session.get(UserAlchemyModel, user.id)
        if not user_model:
            raise ValueError(f"User with id {user.id} not found")
        user_model.name = user.name
        user_model.email = user.email
        user_model.password = user.password
        await self.session.commit()
        await self.session.refresh(user_model)
        return self._to_entity(user_model)

    async def delete(self, user_id: UUID) -> None:
        user_model = await self.session.get(UserAlchemyModel, user_id)
        if not user_model:
            raise ValueError(f"User with id {user_id} not found")
        await self.session.delete(user_model)
        await self.session.commit()

    def _to_entity(self, user_model: UserAlchemyModel) -> User:
        return User(
            id=user_model.id,
            name=user_model.name,
            email=user_model.email,
            password=user_model.password,
            created_at=user_model.created_at,
            updated_at=user_model.updated_at,
        )
