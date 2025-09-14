from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class tarefa(BaseModel):
    id:int
    titulo:str
    concluida: bool = False