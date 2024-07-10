from typing import List
from pydantic import BaseModel
from datetime import datetime


class ProcessCreate(BaseModel):
    user_id: int
    frequency: str
    start_date: datetime
    end_date: datetime
    last_update_date: datetime
    next_update_date: datetime

    erts: List[int]
    contract_types: List[str]


class ProcessRead(ProcessCreate):
    id: int = None

    class Config:
        orm_mode = True
