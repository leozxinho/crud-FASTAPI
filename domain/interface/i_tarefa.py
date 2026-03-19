# domain/interface/i_tarefa_repository.py
from abc import ABC, abstractmethod
from domain.entities.dto.tarefa import Tarefa

class ITarefaRepository(ABC):

    @abstractmethod
    def criar(self, tarefa: Tarefa) -> Tarefa: ...

    @abstractmethod
    def listar(self) -> list[Tarefa]: ...

    @abstractmethod
    def buscar_por_id(self, id: int) -> Tarefa: ...

    @abstractmethod
    def atualizar(self, id: int, tarefa: Tarefa) -> Tarefa: ...

    @abstractmethod
    def deletar(self, id: int) -> None: ...