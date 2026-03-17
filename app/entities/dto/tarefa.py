# Serve para definir o formato dos dados
from pydantic import BaseModel

#Serve para tipar dados
from typing import Optional

class tarefa(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    concluida: bool = False
    