from typing import Callable

from fastapi import FastAPI


def preload_model():
    """
    In order to load model on memory to each worker
    """
    from services.invoice_handler import InvoiceHandler

    InvoiceHandler.generate_invoice()


def create_start_app_handler(app: FastAPI) -> Callable:
    def start_app() -> None:
        preload_model()

    return start_app
