from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.resources import router


def create_app():
    app = FastAPI()

    origins = [
        'http://localhost:8080',
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins = origins,
    )

    app.include_router(router, prefix='/api')

    return app


app = create_app()
