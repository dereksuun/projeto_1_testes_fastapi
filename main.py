from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class TarefaIn(BaseModel):
    titulo: str = Field(min_length=1, max_length=120)
    concluida: bool = False
    prioridade: int = Field(1, ge=1, le=5)

class TarefaOut(TarefaIn):
    id: int

tarefas: List[TarefaOut] = []
_next_id = 1
def prox_id() -> int:
    global _next_id
    i = _next_id
    _next_id += 1
    return i

@app.get("/", tags=["health"])
def root():
    return{"ok": True}

@app.get("/tarefa", response_model=List[TarefaOut])
def listar_tarefas():
    return tarefas

@app.get("/tarefa/{tarefa_id}", response_model=TarefaOut)
def obter_tarefa(tarefa_id: int):
    for t in tarefas:
        if t.id == tarefa_id:
            return t
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.post("/tarefa", response_model=TarefaOut, status_code=201)
def criar_tarefa(dados: TarefaIn):
    nova = TarefaOut(id=prox_id(), **dados.model_dump())
    tarefas.append(nova)
    return nova