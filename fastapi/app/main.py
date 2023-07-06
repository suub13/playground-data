from fastapi import FastAPI
from typing import Union
from src.recommend_system import recommend_api

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Hello World"
    }

@app.post("/recommend")
async def recommend(input_data: list):
    result = recommend_api(input_data)
    return {
        "result": result
    }
