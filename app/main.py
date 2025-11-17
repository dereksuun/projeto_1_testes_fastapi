from typing import Optional, List
from fastapi import FastAPI, HTTPException
from routers import tarefas
from pydantic import BaseModel, Field

app = FastAPI()

app.include_router(tarefas.router)

@app.get("/")
def root():
    return {"message": "Olá!"}