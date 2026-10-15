import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from supabase import create_client

app = FastAPI(title="MAROTHOLI")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY) if SUPABASE_URL and SUPABASE_KEY else None

@app.get("/api/health")
def health():
    return {"status":"ok","brand":"MAROTHOLI"}

@app.get("/")
def root():
    return FileResponse("index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 10000)))
