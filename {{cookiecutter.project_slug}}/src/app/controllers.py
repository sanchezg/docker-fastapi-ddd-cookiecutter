from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.container import Container
from src.domain.repositories {{ cookiecutter.entity_name }}
from src.domain.models import {{ cookiecutter.entity_name }}Repo

router = APIRouter()


@router.get("/")
@inject
async def index(
    *args,
    repo: {{ cookiecutter.entity_name }}Repo = Depends(Provide[Container.{{ cookiecutter.entity_slug }}_repo]),
) -> {{ cookiecutter.entity_name }} | list[SomeType] | str:
    results = await repo.get(*args)
    return results
