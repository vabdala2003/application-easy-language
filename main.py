import logging
import sys

from PySide6.QtWidgets import QApplication

from app.config.configure_logging import configure_logging
from app.core.custom_exceptions import EasyLanguageException
from app.ui.main_screen import MainScreen


def safe_logging_setup():
    """
    Safely sets up logging for the application.
    If logging configuration fails, it raises the custom error 'ConfigurationException'.
    """
    configure_logging()
    return logging.getLogger(__name__)


def main():
    try:
        logger = safe_logging_setup()
        logger.info("Starting the application")

        app = QApplication(sys.argv)

        initial_screen = MainScreen()
        initial_screen.show()

        exit_code = app.exec()

        logger.info("Application terminated successfully")

        sys.exit(exit_code)

    except EasyLanguageException as e:
        logging.error(f"Application terminated with an EasyLanguage error: {e}")
        raise

    except Exception as e:
        logging.error(f"Application terminated with an unknown error: {e}")
        raise


if __name__ == "__main__":
    main()
