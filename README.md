# docker-fastapi-ddd-cookiecutter
A cookicutter with FastAPI and Docker, with DDD directory structure and repository pattern.

# Installation instructions

1. Install cookiecutter:

`$ python3 -m pip install cookiecutter`

2. Create an empty project with this repository as source:

`$ python3 -m cookiecutter git@github.com:sanchezg/docker-fastapi-ddd-cookiecutter.git`

3. Fill the prompt when requested as needed:

```
[1/7] project_name (FastAPI App with Docker and DDD): Some Name
[2/7] project_slug (some_name):
[3/7] entity_name (SomeEntity): User
[4/7] entity_slug (user):
[5/7] add_postgresql [y/n] (y):
[6/7] add_elasticsearch [y/n] (n): y
[7/7] add_redis [y/n] (n): y
```

# Project first steps

Add the needed requirements with poetry (recommended):

`$ python3 -m pip install poetry`
`$ poetry init`
`$ poetry add fastapi uvicorn python-dotenv dependency-injector asyncpg sqlalchemy redis elasticsearch`
