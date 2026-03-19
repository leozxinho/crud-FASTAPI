import asyncio
from infrastructure.database_mysql.mysql_connection import engine, Base
from domain.entities.models.tarefa import TarefaModel

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
asyncio.run(create_tables())