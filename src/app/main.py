import uvicorn
from fastapi import FastAPI

from app.settings import Settings

settings = Settings()
app = FastAPI()


def main():
    uvicorn.run(app, host=settings.host_address, port=settings.port, log_level="debug")
