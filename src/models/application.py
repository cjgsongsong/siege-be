"""Application-related models."""

from pydantic import BaseModel

class ApplicationDetails(BaseModel):
    """Model of application details."""

    description: str
    title: str
    version: str
