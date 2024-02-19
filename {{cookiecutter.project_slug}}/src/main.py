from fastapi import FastAPI

from src.app.controllers import router
from src.infra import entity_mappings  # noqa
from src.container import Container


def create_app() -> FastAPI:
    container = Container()

    app = FastAPI()
    app.container = container  # type: ignore
    app.include_router(router)
    return app

app = create_app()
