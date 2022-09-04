from core.errors import InvoiceException
from loguru import logger


class InvoiceHandler(object):
    
    @classmethod
    def generate_invoice(file_path):
        if file_path is None:
            raise InvoiceException(f"'{file_path}' url is missing")
        return file_path