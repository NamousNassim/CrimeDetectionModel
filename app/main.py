from fastapi import FastAPI

import uvicorn

app = FastAPI()

@app.get("/")
def main():
    return {"message": "API model"}

@app.get("/{local}")
def local(local: str):
    return {"message": f"Localsiation {local}"}