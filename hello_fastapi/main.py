"""FastAPI Hello World App"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    """root endpoint"""
    return {"message": "Hello FastAPI!"}
