from typing import Optional
from pydantic import BaseModel

#Base model
class FileOptions(BaseModel):
    FileName: str
    FileDesc: str = "Upload for demonstration"
    FileType: Optional[str]