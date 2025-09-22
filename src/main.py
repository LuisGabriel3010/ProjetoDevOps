from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi import HTTPException

app = FastAPI()

class Tarefa(BaseModel):
    id:int
    nome:str
    concluida: bool = False

class Usuario(BaseModel):
    username:str
    senha:str
    

tarefas :List[Tarefa] = []

@app.post("/tarefa/",response_model=Tarefa)
def criar_tarefa(tarefa:Tarefa):
    tarefas.append(tarefa)
    return tarefa

@app.get("/tarefa/",response_model=List[Tarefa])
def listar_tarefas():
    return tarefas

@app.get("/tarefa/{tarefa_id}" ,response_model=Tarefa)
def obter_tarefa(tarefa_id:int):
    for tarefa in tarefas:
        if tarefa.id == tarefa_id:
            return tarefa
        raise HTTPException(status_code=404, detail="Não há tarefas")


@app.put("/tarefa/{tarefa_id}" ,response_model=Tarefa)
def atualizar_tarefa(tarefa_id:int,tarefa:Tarefa):
    for i,t in enumerate(tarefas):
        if t.id == tarefa_id:
            tarefas[i] = tarefa
            return tarefa
        raise HTTPException(status_code=404, detail="Não foi possivel atualizar tarefa")

@app.delete("/tarefa/{tarefa_id}" ,response_model=Tarefa)
def deletar_tarefa(tarefa_id:int):
    for i, t  in enumerate(tarefas):
        if t.id == tarefa_id:
            tarefas.pop(i)
            return {"mensagem": "Tarefa removida"}



@app.get("/tarefa/concluidas",response_model=List[Tarefa])
def listar_tarefas_concluidas(tarefa_id:int):
    for tarefa in tarefas:
        if tarefa.id == tarefa_id:
            tarefa.concluida = True
            return tarefa
        raise HTTPException(status_code=404, detail="Não há tarefas concluídas")