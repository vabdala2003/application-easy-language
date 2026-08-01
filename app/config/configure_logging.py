
import logging
from pythonjsonlogger.json import JsonFormatter
from pathlib import Path
from app.core.custom_exceptions import ConfigurationException


def configure_logging(file: bool = True):
    """
    Configures logging for the application.

    Args:
        file (bool): If True, logs will be written to a file. If False, logs will be printed to the console only.
    """

    try:
        handlers = []
        stream_handler = logging.StreamHandler()

        stream_handler_formatter = logging.Formatter(
            fmt=" | ".join(get_format_elements()),
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        stream_handler.setFormatter(stream_handler_formatter)

        handlers.append(stream_handler)

        if file:
            logs_path = Path('app', 'logs')
            logs_path.mkdir(parents=True, exist_ok=True)

            file_handler = logging.FileHandler(logs_path / 'app.log')
            file_handler.setFormatter(
                JsonFormatter(
                    " ".join(get_format_elements()),
                    datefmt="%Y-%m-%d %H:%M:%S",
                )
            )
            handlers.append(file_handler)

        logging.basicConfig(
            level=logging.DEBUG,
            handlers=handlers,
            datefmt="%Y-%m-%d %H:%M:%S",
            force=True
        )

    except Exception as e:
        raise ConfigurationException(f"Failed to configure logging: {e}") from e

def get_format_elements():
    format_elements = [
        "%(asctime)s",
        "%(levelname)s",
        "%(funcName)s",
        "%(module)s",
        "%(message)s"
    ]
    return format_elements
