from urllib.parse import quote_plus

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from infrastructure.config import get_environment_variables
import urllib.parse

env = get_environment_variables()


DATABASE_URL = "{}://{}:{}@{}:{}/{}".format(
    "mysql+aiomysql",
    env.DB_LOGIN,
    urllib.parse.quote_plus(env.DB_PASSWORD),
    env.DB_NAME
)

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_session():
    async with AsyncSessionLocal() as session:
        yield session

class Base(DeclarativeBase):
    pass