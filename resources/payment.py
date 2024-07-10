from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from schemas.payment import PaymentCreate
from models.payment import PaymentModel
from database import get_db

router = APIRouter()


@router.post("/create/")
async def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    new_payment = PaymentModel(**payment.dict())
    try:
        db.add(new_payment)
        db.commit()
    except SQLAlchemyError:
        raise HTTPException(500, detail="An error occurred while inserting the payment data to db")
    return {"message": "payment created"}, 200
