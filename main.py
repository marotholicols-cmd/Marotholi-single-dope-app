from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/api/health")
def health():
    return {"status": "ok", "brand": "MAROTHOLI"}

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>MAROTHOLI</title>
    <style>
    body{margin:0;background:#1a0a2e;color:#fff;font-family:sans-serif;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh;text-align:center}
    h1{font-size:50px;margin:0;letter-spacing:6px;color:#d9a0ff;text-shadow:0 0 20px #a020f0}
    h2{letter-spacing:12px;font-weight:300;margin:10px 0 40px;opacity:.8}
    .btn{background:#a020f0;color:#fff;padding:18px 65px;border-radius:30px;border:none;font-size:20px;box-shadow:0 0 30px #a020f0;cursor:pointer;letter-spacing:3px}
    .btn:active{transform:scale(.95)}
    p{margin-top:50px;opacity:.4;font-size:12px;letter-spacing:2px}
    </style>
    </head>
    <body>
    <h1>MAROTHOLI</h1>
    <h2>SINGLE DOPE</h2>
    <button class="btn" onclick="document.body.innerHTML='<h1 style=margin-top:40vh>🔥 WELCOME FAM 🔥<br><br><a href=/ style=color:#d9a0ff>BACK</a></h1>'">ENTER</button>
    <p>EST. 2026 • MASERU, LESOTHO</p>
    </body>
    </html>
    """