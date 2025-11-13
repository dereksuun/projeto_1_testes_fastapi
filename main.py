from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Olá"}

@app.get("/lista/{item_id}")
def read_list(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}