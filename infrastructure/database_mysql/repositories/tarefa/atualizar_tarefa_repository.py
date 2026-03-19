from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from domain.entities.models.tarefa import TarefaModel


class AtualizarTarefaRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def atualizar_tarefa(self, id: int, tarefa: TarefaModel):
        async with self.session as session:
            stmt = (
                update(TarefaModel)
                .where(TarefaModel.id == id)
                .values(
                    titulo=tarefa.titulo,
                    descricao=tarefa.descricao,
                    concluido=tarefa.concluido,
                )
            )
        await self.session.execute(stmt)
        await self.session.commit()
        
        result = await session.execute(select(TarefaModel).where(TarefaModel.id == id))
        return result.scalar_one_or_none()