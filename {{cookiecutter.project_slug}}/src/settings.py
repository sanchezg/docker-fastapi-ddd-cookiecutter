import os

from dotenv import load_dotenv

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Load minimum env vars needed for .env
env = os.environ.get("ENV", "LOCAL").lower()

# Load .env before other settings to properly set environment defaults from the
# config (those not already set at the OS/instance)
dotenv_path = BASE_DIR + "/config/.env." + env
load_dotenv(dotenv_path=dotenv_path)

BASE_URL = os.environ.get("BASE_URL")
DEBUG = bool(os.environ.get("DEBUG"))

IS_PROD_ENV = env == "prod"
IS_LOCAL_ENV = env == "local"
IS_DEV_ENV = env == "dev"

{% if cookiecutter.add_elasticsearch %}ES_URI = os.environ.get("ES_URI", "http://elasticsearch:9200")
ES_CHUNK_SIZE = int(os.environ.get("ES_CHUNK_SIZE", 100))
ES_MAX_SIZE = int(os.environ.get("ES_MAX_SIZE", 100))
{% endif %}

{% if cookiecutter.add_postgresql %}POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "postgres")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", 5432)
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_URI = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
{% endif %}

{% if cookiecutter.add_redis %}REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
{% endif %}

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(asctime)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "default": {"handlers": ["default"], "level": "DEBUG" if DEBUG else "INFO"},
    },
}
