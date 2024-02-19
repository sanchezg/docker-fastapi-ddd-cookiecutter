from sqlalchemy import Column, DateTime
from sqlalchemy import Integer, String, Table, text
# from sqlalchemy.orm import relationship

from src.domain.models import {{ cookiecutter.entity_name }}
from src.infra.database import mapper_registry

mapper_params = {
    "eager_defaults": True,
}

table_params = {
    "mysql_charset": "utf8mb4",
    "mysql_collate": "utf8mb4_unicode_ci",
}

{{ cookiecutter.entity_slug }}_table = Table(
    "{{ cookiecutter.entity_slug }}s",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("created_at", DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP")),
    Column(
        "updated_at",
        DateTime,
        nullable=True,
        onupdate=text("CURRENT_TIMESTAMP"),
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    ),
    **table_params,
)

mapper_registry.map_imperatively(
    {{ cookiecutter.entity_name }},
    {{ cookiecutter.entity_slug }}_table,
    **mapper_params,
    properties={
        # Add any FK relationships here
        # "organizations": relationship(Organization, back_populates="{{ cookiecutter.entity_slug }}", lazy="subquery"),
    },
)
