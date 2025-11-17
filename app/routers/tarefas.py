from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from schemas.tarefas import TarefaCreate, TarefaOut, TarefaUpdate

router = APIRouter(prefix="/tarefas", tags=["tarefas"])

_fake_db: dict[int, TarefaOut] = {}
_next_id = 1

def _get_next_id() -> int:
    global _next_id
    _next_id +=1
    return _next_id - 1

@router.get("/", response_model=List[TarefaOut])
def listar_tarefa() -> List[TarefaOut]:
    return list(_fake_db.values())

@router.post("/", response_model=TarefaOut, status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa: TarefaCreate) -> TarefaOut:
    new_id = _get_next_id()
    tarefa_out = TarefaOut(id=new_id, **tarefa.model_fields_set, **tarefa.model_dump())
    _fake_db[new_id] = tarefa_out
    return tarefa_out