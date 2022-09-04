from fastapi import APIRouter, HTTPException,  Request, File, UploadFile, Depends
from loguru import logger
from models.health import HealthResponse
from models.invoice_file import FileOptions
from services.invoice_handler import InvoiceHandler as inv

router = APIRouter()

@router.post(
    "/invoice", response_model=HealthResponse, name="invoice:post-data",
)
async def invoice(file: FileOptions = Depends(), data: UploadFile = File(...)):
    try:
        data_options = file.dict()
            
        result = "Uploaded Filename: {}. JSON Payload    {}".format(data.filename, data_options)
        logger.info(result)
        inv.generate_invoice()
        is_health = True
        return HealthResponse(status=is_health)
    except Exception as ex:
        logger.info(f"Errpr : {ex}")
        raise HTTPException(status_code=404, detail="Unhealthy")

