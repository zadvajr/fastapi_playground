"""Path Parameters"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    """Enpoint to Read Item"""
    return {"item_id": item_id}
