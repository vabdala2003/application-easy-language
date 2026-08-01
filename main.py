import logging
from app.config.configure_logging import configure_logging
from app.core.custom_exceptions import EasyLanguageException


def safe_logging_setup():
    """
    Safely sets up logging for the application.
    If logging configuration fails, it raises the custom error 'ConfigurationException'.
    """
    configure_logging()
    return logging.getLogger(__name__)

def initialize_app():
    """
    Initializes the application.
    """
    pass

def main():
    try:
        logger = safe_logging_setup()
        logger.info("Starting the application")

        initialize_app()

        logger.info("Application terminated successfully")

    except EasyLanguageException as e:
        logging.error(f"An EasyLanguage error occurred: {e}")
        raise

    except Exception as e:
        logging.error(f"An unknown error occurred: {e}")
        raise


if __name__ == "__main__":
    main()
