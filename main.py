from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/api/health")
def health():
    return {"status": "ok", "brand": "MAROTHOLI"}

@app.get("/")
def home():
    return FileResponse("index.html")