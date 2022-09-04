from fastapi import APIRouter

from api.routes import invoice_generator as invoice
from api.routes import base as home

router = APIRouter()
router.include_router(invoice.router, tags=["invoice"], prefix="/v1")
router.include_router(home.router, tags=["home"], prefix="/v1")
