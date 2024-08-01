from fastapi import FastAPI
from model.router import router as model_router
from settings import settings

app = FastAPI()
app.include_router(model_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, host=settings.server_host, port=settings.server_port)