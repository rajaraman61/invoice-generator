from typing import Callable

from fastapi import FastAPI
def load_health_checker():
    """
    In order to load invoice generator to each worker
    """
    from services.health_check import HealthHandler

    HealthHandler.check_health()

def create_start_app_handler(app: FastAPI) -> Callable:
    def start_app() -> None:
        load_health_checker()

    return start_app
