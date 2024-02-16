from src.domain.models import {{ cookiecutter.entity_name }}
from src.domain.repositories import {{ cookiecutter.entity_name }}Repo
{% if cookiecutter.add_elasticsearch %}from src.infra.elasticsearch import ESRepo{% endif %}
{% if cookiecutter.add_postgresql %}from src.infra.sqlalchemy import SqlAlchemyRepo{% endif %}
{% if cookiecutter.add_redis %}from src.infra.redis import RedisRepo{% endif %}


{% if cookiecutter.add_elasticsearch %}
class ES{{ cookiecutter.entity_name }}Repo(ESRepo, {{ cookiecutter.entity_name }}Repo):
    entity = {{ cookiecutter.entity_name }}
    index_name = "{{ cookiecutter.entity_slug }}s"

    async def get(self, *args, **kwargs) -> list[{{ cookiecutter.entity_name }}] | None:
        # TODO: Implement this method
        ...

    async def insert(self, **kwargs) -> int | None:
        # TODO: implement this method
        ...
{% endif %}


{% if cookiecutter.add_postgresql %}
class Postgres{{ cookiecutter.entity_name }}Repo(SqlAlchemyRepo, {{ cookiecutter.entity_name }}Repo):
    entity = {{ cookiecutter.entity_name }}
    table_name = "{{ cookiecutter.entity_slug }}s"

    async def get(self, *args, **kwargs) -> list[{{ cookiecutter.entity_name }}] | None:
        # TODO: Implement this method
        ...

    async def insert(self, **kwargs) -> int | None:
        # TODO: implement this method
        ...
{% endif %}


{% if cookiecutter.add_redis %}
class Redis{{ cookiecutter.entity_name }}Repo(ESRepo, {{ cookiecutter.entity_name }}Repo):
    entity = {{ cookiecutter.entity_name }}

    async def get(self, *args, **kwargs) -> list[{{ cookiecutter.entity_name }}] | None:
        # TODO: Implement this method
        ...

    async def insert(self, **kwargs) -> int | None:
        # TODO: implement this method
        ...
{% endif %}
