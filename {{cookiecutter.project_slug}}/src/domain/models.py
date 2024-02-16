from dataclasses import dataclass


@dataclass
class {{ cookiecutter.entity_name }}:
    id: int
    name: str
    created_at: str
    updated_at: str
