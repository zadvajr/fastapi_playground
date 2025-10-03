"""Path Parameters containing paths"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """Read file"""
    return {"file_path": file_path}
