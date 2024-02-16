import abc
from typing import Generic, Optional, TypeVar

from src.domain.models import {{ cookiecutter.entity_name }}

T = TypeVar("T")


class AbstractRepo(abc.ABC, Generic[T]):
    @abc.abstractmethod
    async def get(self, **kwargs) -> Optional[T]:
        pass

    @abc.abstractmethod
    async def insert(self, **kwargs) -> None:
        pass


class {{ cookiecutter.entity_name }}Repo(AbstractRepo[{{ cookiecutter.entity_name }}], metaclass=abc.ABCMeta):
    pass
