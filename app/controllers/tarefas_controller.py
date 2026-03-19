from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from domain.entities.dto.response.tarefas_response import TarefaCreate, TarefasResponse
from domain.entities.dto.tarefa import TarefaDelete, TarefaUpdate
from infrastructure.database_mysql.mysql_connection import get_session
from infrastructure.database_mysql.repositories.tarefa.atualizar_tarefa_repository import AtualizarTarefaRepository
from infrastructure.database_mysql.repositories.tarefa.buscar_tarefa_id_repository import BuscarTarefaIDRepository
from infrastructure.database_mysql.repositories.tarefa.deletar_tarefa_repository import DeletarTarefaRepository
from infrastructure.database_mysql.repositories.tarefa.listar_tarefa_repository import ListarTarefaRepository
from infrastructure.database_mysql.repositories.tarefa.criar_tarefa_repository import CriarTarefaRepository
from domain.usecase.atualizar_tarefa_usecase import AtualizarTarefaUsecase
from domain.usecase.buscar_tarefa_id_usecase import BuscarTarefaIDUsecase
from domain.usecase.deletar_tarefa_usecase import DeletarTarefaUsecase
from domain.usecase.listar_tarefas_usecase import ListarTarefaUsecase
from domain.usecase.criar_tarefa_usecase import CriarTarefaUsecase


with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()

router = APIRouter(
    tags=["Tarefas"],
    prefix="/api/v1",
)


# Listar todas as tarefas
@router.get("/tarefas", response_model=List[TarefasResponse])
async def listar_tarefas(session: AsyncSession = Depends(get_session)):
   repository = ListarTarefaRepository(session)
   usecase = ListarTarefaUsecase(repository)
   tarefas = await usecase.executar()
   return tarefas


# Buscar tarefa por ID
@router.get("/tarefas/{id}", response_model=TarefasResponse)
async def buscar_tarefa(id: int, session: AsyncSession = Depends(get_session)):
    repository = BuscarTarefaIDRepository(session)
    usecase = BuscarTarefaIDUsecase(repository)
    return await usecase.execute(id)
    
 
# Criar uma nova tarefa
@router.post("/tarefas", response_model=TarefasResponse)
async def criar_tarefa(tarefa_model: TarefaCreate, session: AsyncSession = Depends(get_session)):
    repository = CriarTarefaRepository(session)
    usecase = CriarTarefaUsecase(repository)
    return await usecase.executar(tarefa_model)
                                       
                                       
# Atualizar uma tarefa existente
@router.put("/tarefas/{id}", response_model=TarefasResponse)
async def atualizar_tarefa(id: int, tarefa_data: TarefaUpdate, session: AsyncSession = Depends(get_session)):
    repository = AtualizarTarefaRepository(session)
    usecase = AtualizarTarefaUsecase(repository)
    tarefas = await usecase.execute(id, tarefa_data)
    return tarefas

# Excluir uma tarefa
@router.delete("/tarefas/{id}", status_code=200)
async def excluir_tarefa(id: int, session: AsyncSession = Depends(get_session)):
    repository = DeletarTarefaRepository(session)
    usecase = DeletarTarefaUsecase(repository)
    await usecase.execute(id)
    return {"detail": "Tarefa excluída com sucesso."}