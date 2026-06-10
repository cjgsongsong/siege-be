"""`siege-be` entry point."""

from enumerations.application import Application
from fastapi import FastAPI
from uvicorn import run

application = FastAPI(
    description = Application.DESCRIPTION,
    title = Application.TITLE,
    version = Application.VERSION
)

if __name__ == Application.DIRECT_EXECUTION_MODULE:
    run(
        app = Application.ASGI_APPLICATION,
        reload = True
    )
