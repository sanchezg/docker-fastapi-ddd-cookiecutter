from dependency_injector import containers, providers
{% if cookiecutter.add_redis %}import redis.asyncio as aioredis{% endif %}

import settings
{% if cookiecutter.add_elasticsearch %}from src.infra.repositories import ES{{ cookiecutter.entity_name }}Repo{% endif %}
{% if cookiecutter.add_postgresql %}from src.infra.repositories import Postgres{{ cookiecutter.entity_name }}Repo
from src.infra.database import async_session{% endif %}
{% if cookiecutter.add_redis %}from src.infra.repositories import Redis{{ cookiecutter.entity_name }}Repo{% endif %}


class Container(containers.DeclarativeContainer):
    """Container to serve all the containers related to the app"""

    # Set wiring between endpoints and injected repositories
    wiring_config = containers.WiringConfiguration(modules=[".app.controllers"])

    # DB clients
    {% if cookiecutter.add_elasticsearch %}es_client = providers.Factory(AsyncElasticsearch, settings.ES_URI){% endif %}
    {% if cookiecutter.add_redis %}redis_client = providers.Singleton(
        aioredis.Redis,
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        password=settings.REDIS_PASSWORD
    ){% endif %}

    # Repositories
    {% if cookiecutter.add_postgresql %}{{ cookiecutter.entity_slug }}_repo = providers.Factory(
        Postgres{{ cookiecutter.entity_name }}Repo,
        session=async_session,
    ){% endif %}
    {% if cookiecutter.add_elasticsearch %}{{ cookiecutter.entity_slug }}_docs_repo = providers.Factory(
        ES{{ cookiecutter.entity_name }}Repo,
        es_client=es_client,
    ){% endif %}
    {% if cookiecutter.add_redis %}{{ cookiecutter.entity_slug }}_cache_repo = providers.Factory(
        Redis{{ cookiecutter.entity_name }}Repo,
        client=redis_client,
    ){% endif %}
