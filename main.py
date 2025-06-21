from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "¡API Forex Institucional funcionando en Codespaces!"}
