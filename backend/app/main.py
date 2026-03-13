from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

app = FastAPI(
    title="Pipeimob Challenge API",
    description="Central de Enquetes — Teste Técnico Pipeimob",
    version="1.0.0"
)

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Pipeimob Challenge API"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}


# TODO: Inclua seus routers aqui
# Exemplo:
# from app.api.v1.routes.poll_controller import router as poll_router
# from app.api.v1.routes.auth_controller import router as auth_router
# app.include_router(auth_router, prefix="/api/v1", tags=["Auth"])
# app.include_router(poll_router, prefix="/api/v1", tags=["Polls"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
