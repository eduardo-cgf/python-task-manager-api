
from fastapi import FastAPI

# Criamos nossa aplicação
app = FastAPI(
    title="Task Manager API",
    description="A simple API to manage tasks.",
    version="0.1.0",
)


# Primeira rota: página inicial
@app.get("/")
def home():
    return {
        "message": "Welcome to the Task Manager API!"
    }


# Segunda rota: verificar se a API está funcionando
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }