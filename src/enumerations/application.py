"""Application-related enumerations."""

from enum import StrEnum

class Application(StrEnum):
    """Enumeration of application-related constants."""

    ASGI_APPLICATION = "main:application"
    DIRECT_EXECUTION_MODULE = "__main__"
    DESCRIPTION = "Backend application of personal website."
    TITLE = "siege-be"
    VERSION = "0.0.0"
