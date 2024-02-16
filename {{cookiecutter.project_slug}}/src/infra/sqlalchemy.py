from typing import Any, Iterable, Optional

from sqlalchemy import select

from src.domain.repositories import T, AbstractRepo


class SqlAlchemyRepo(AbstractRepo):
    entity = None

    def __init__(self, session):
        self.session = session

    def _get_base_query(self, *args, **kwargs):
        query = select(self.entity).where(*args)
        return query

    def _add(self, *entities: T):
        self.session.add_all(entities)

    async def get(self, entity_id: str) -> Optional[Any]:
        query = self._get_base_query(*(self.entity.id == entity_id,))
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_all(
        self, *filters, order_by: Optional[str] = None, pagination: Optional[dict] = None,
    ) -> Iterable:
        query = self._get_base_query(*filters)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_one(self, *filters) -> Iterable:
        query = self._get_base_query(*filters)
        result = await self.session.execute(query)
        return result.scalars().one_or_none()

    async def remove(self, *entities: T):
        for e in entities:
            await self.session.delete(e)
