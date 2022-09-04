from core.errors import InvoiceException
from loguru import logger


class HealthHandler(object):
    
    @classmethod
    def check_health():
        is_healthy = True
        return is_healthy