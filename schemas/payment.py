from typing import Optional
from pydantic import BaseModel, condecimal
from datetime import datetime
from decimal import Decimal


class PaymentCreate(BaseModel):
    status: str
    process_id: int
    update_date: datetime
    amount: condecimal(gt=Decimal('0.00'))
    type: str


class PaymentRead(PaymentCreate):
    id: int = None

    class Config:
        orm_mode = True
