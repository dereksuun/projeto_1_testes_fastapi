from pydantic import BaseModel, Field
from typing import Optional

class TarefaBase(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    done: bool = False
    priority: int = Field(1, ge=1, le=5)

class TarefaCreate(TarefaBase):
    pass

class TarefaUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None
    priority: Optional[int] = None

class TarefaOut(TarefaBase):
    id: int