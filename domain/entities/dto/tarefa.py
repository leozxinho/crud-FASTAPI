from pydantic import BaseModel
from typing import Optional

class Tarefa(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    concluido: bool = False
    
class TarefaUpdate(BaseModel):
    titulo: str
    descricao: str
    concluido: bool
    
class TarefaDelete(BaseModel):
    id: int
