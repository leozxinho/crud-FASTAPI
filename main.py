from app.controllers import tarefas_controller
from fastapi import FastAPI

app = FastAPI(
    title="Api de tarefas",
    version="1.0.0",
    description="""
Api para gerenciamento de TAREFAS!

<a href="https://github.com/seu-user/seu-repo/blob/main/README.md" target="_blank">
👉 Ver documentação completa (README.md)
</a>
"""
)


app.include_router(tarefas_controller.router)