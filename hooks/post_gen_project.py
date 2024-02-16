import os
import sys


def add_docker_services():
    compose_file = "docker/docker-compose.yml"

    add_postgres = "{{ cookiecutter.add_postgresql }}" == "True"
    add_elasticsearch = "{{ cookiecutter.add_elasticsearch }}" == "True"
    add_redis = "{{ cookiecutter.add_redis }}" == "True"

    if add_postgres or add_elasticsearch or add_redis:
        with open(compose_file, "a") as f:
            f.write("    depends_on:\n")
            if add_postgres:
                f.write("      - postgres\n")
            if add_elasticsearch:
                f.write("      - elasticsearch\n")
            if add_redis:
                f.write("      - redis\n")
            f.write("\n")

            if add_postgres:
                f.write("  postgres:\n")
                f.write("    image: postgres:13\n")
                f.write("    environment:\n")
                f.write("      POSTGRES_DB: {{ cookiecutter.project_slug }}\n")
                f.write("      POSTGRES_USER: {{ cookiecutter.project_slug }}\n")
                f.write("      POSTGRES_PASSWORD: {{ cookiecutter.project_slug }}\n")
                f.write("    ports:\n")
                f.write("      - 5432:5432\n")
                f.write("    volumes:\n")
                f.write("      - ./data/postgres:/var/lib/postgresql/data\n")
                f.write("\n")

            if add_elasticsearch:
                f.write("  elasticsearch:\n")
                f.write("    image: elasticsearch:8.12.1\n")
                f.write("    environment:\n")
                f.write("      - discovery.type=single-node\n")
                f.write('      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"\n')
                f.write("      - xpack.security.enabled=false\n")
                f.write("    ports:\n")
                f.write("      - 9200:9200\n")
                f.write("    volumes:\n")
                f.write("      - ./data/elasticsearch:/usr/share/elasticsearch/data\n")
                f.write("\n")

            if add_redis:
                f.write("  redis:\n")
                f.write("    image: redis:6.2.5\n")
                f.write("    ports:\n")
                f.write("      - 6379:6379\n")
                f.write("    volumes:\n")
                f.write("      - ./data/redis:/data\n")
                f.write("\n")


def remove_unwanted_repositories():
    add_postgres = "{{ cookiecutter.add_postgresql }}" == "True"
    add_elasticsearch = "{{ cookiecutter.add_elasticsearch }}" == "True"
    add_redis = "{{ cookiecutter.add_redis }}" == "True"

    if not add_postgres:
        os.remove("src/infra/sqlalchemy.py")
        os.remove("src/infra/database.py")
    if not add_elasticsearch:
        os.remove("src/infra/elasticsearch.py")
    if not add_redis:
        os.remove("src/infra/redis.py")


def add_env_variables():
    add_postgres = "{{ cookiecutter.add_postgresql }}" == "True"
    add_elasticsearch = "{{ cookiecutter.add_elasticsearch }}" == "True"
    add_redis = "{{ cookiecutter.add_redis }}" == "True"

    with open("src/config/.env.local", "a") as f:
        if add_elasticsearch:
            f.write("ES_URI=http://elasticsearch:9200\n")
            f.write("ES_CHUNK_SIZE=100\n")
            f.write("ES_MAX_SIZE=100\n")
        if add_postgres:
            f.write("POSTGRES_USER={{ cookiecutter.project_slug }}\n")
            f.write("POSTGRES_PASSWORD={{ cookiecutter.project_slug }}\n")
            f.write("POSTGRES_HOST=postgres\n")
            f.write("POSTGRES_PORT=5432\n")
            f.write("POSTGRES_DB={{ cookiecutter.project_slug }}\n")
        if add_redis:
            f.write("REDIS_HOST=redis\n")
            f.write("REDIS_PORT=6379\n")
            f.write("REDIS_PASSWORD=\n")


if __name__ == "__main__":
    add_docker_services()
    remove_unwanted_repositories()
    add_env_variables()
