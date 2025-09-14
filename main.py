from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tarefa(BaseModel):
    id:int
    titulo:str
    concluida: bool = False

tarefas :List[Tarefa] = []

@app.post("/tarefa/",response_model=Tarefa)
def criar_tarefa(tarefa:Tarefa):
    tarefas.append(tarefa)
    return tarefa

