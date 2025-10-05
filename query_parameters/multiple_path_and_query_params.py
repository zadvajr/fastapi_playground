"""Multiple Path and Query Parameters"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_id(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    """Read User Item"""
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item
