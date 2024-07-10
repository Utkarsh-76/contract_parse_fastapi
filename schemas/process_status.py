from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class ProcessStatusCreate(BaseModel):
    process_id: int
    process_start: datetime
    process_end: datetime
    current_status: str


class ProcessStatusRead(ProcessStatusCreate):
    id: int = None

    class Config:
        orm_mode = True
