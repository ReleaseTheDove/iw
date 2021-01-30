from fastapi import FastAPI
from app.resources import router


def create_app():
    app = FastAPI()


    app.include_router(router, prefix='/api')

    return app

app = create_app()

