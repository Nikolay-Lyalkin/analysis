import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

load_dotenv()

# URL для подключения
dsn = os.getenv(
    "DATABASE_URL", "mysql+pymysql://root:9998441653Qq@localhost:3306/ramir_1.0"
)

# Создаём асинхронный движок
engine = create_engine(
    dsn, echo=False, pool_pre_ping=True, pool_recycle=300, pool_size=10, max_overflow=20
)

# Создаём фабрику сессий
local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency для получения сессии БД
def get_session() -> Session:
    """Получение синхронной сессии БД"""
    session = local_session()
    try:
        return session
    except Exception:
        session.close()
        raise


def get_session_ctx() -> Session:
    """Альтернатива для использования вне FastAPI"""
    return get_session()
