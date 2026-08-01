class EasyLanguageException(Exception):
    """Custom exception for EasyLanguage-related errors."""

    def __init__(self, message="An EasyLanguage error occurred"):
        self.message = message
        super().__init__(self.message)


class ConfigurationException(EasyLanguageException):
    """Custom exception for configuration-related errors."""

    def __init__(self, message="A configuration error occurred"):
        self.message = message
        super().__init__(self.message)


class CoreException(EasyLanguageException):
    """Custom exception for core application errors."""

    def __init__(self, message="A core application error occurred"):
        self.message = message
        super().__init__(self.message)


class ValidationException(EasyLanguageException):
    """Custom exception for validation-related errors."""

    def __init__(self, message="A validation error occurred"):
        self.message = message
        super().__init__(self.message)


class IntegrationException(EasyLanguageException):
    """Custom exception for integration-related errors."""

    def __init__(self, message="An integration error occurred"):
        self.message = message
        super().__init__(self.message)


class DatabaseException(EasyLanguageException):
    """Custom exception for database-related errors."""

    def __init__(self, message="A database error occurred"):
        self.message = message
        super().__init__(self.message)


class OpenAIException(EasyLanguageException):
    """Custom exception for OpenAI-related errors."""

    def __init__(self, message="An OpenAI error occurred"):
        self.message = message
        super().__init__(self.message)


class ModelException(EasyLanguageException):
    """Custom exception for model-related errors."""

    def __init__(self, message="A model error occurred"):
        self.message = message
        super().__init__(self.message)


class ServiceException(EasyLanguageException):
    """Custom exception for service-related errors."""

    def __init__(self, message="A service error occurred"):
        self.message = message
        super().__init__(self.message)


class UIException(EasyLanguageException):
    """Custom exception for UI-related errors."""

    def __init__(self, message="A UI error occurred"):
        self.message = message
        super().__init__(self.message)
