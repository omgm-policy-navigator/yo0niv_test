from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine

from app.core.config import Settings


def create_database_engine(settings: Settings) -> AsyncEngine:
    return create_async_engine(settings.sqlalchemy_database_url, pool_pre_ping=True)


def create_session_factory(settings: Settings) -> async_sessionmaker:
    return async_sessionmaker(create_database_engine(settings), expire_on_commit=False)
