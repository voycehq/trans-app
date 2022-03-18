from pydantic import BaseModel
from config import base_dir


class LogConfig(BaseModel):
    """
    Logging configuration to be set for the server
    """

    SERVER_LOGGER: str = "server"
    LOG_FORMAT: str = f"%(levelprefix)s | %(asctime)s | %(filename)s:%(lineno)d | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    DATABASE_LOGGER: str = "database"

    # Logging config
    version = 1
    disable_existing_loggers = False

    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%d-%b-%Y (%Y-%m-%d) %H:%M:%S %p",
        },
    }
    handlers = {
        "console": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "file": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "formatter": "default",
            "filename": f'{base_dir}/app/logs/server.log',
        },
    }

    loggers = {"server": {"handlers": ["console", "file"], "level": LOG_LEVEL}}
