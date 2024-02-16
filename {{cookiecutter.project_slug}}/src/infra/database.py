from asyncio import current_task

from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session, create_async_engine
from sqlalchemy.orm import registry, sessionmaker

from src import settings


def get_database_session(database_url: str):
    engine = create_async_engine(
        database_url,
        encoding="utf8",
        echo=settings.DEBUG,
        pool_pre_ping=True,
    )

    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    scoped_session = async_scoped_session(async_session, scopefunc=current_task)
    return scoped_session, async_session, engine


scoped_session, async_session, engine = get_database_session(settings.POSTGRES_URI)
mapper_registry = registry()
