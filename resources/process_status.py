from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from schemas.process_status import ProcessStatusCreate
from models.process_status import ProcessStatusModel
from database import get_db

router = APIRouter()


@router.post("/create/")
async def create_process_status(process_status: ProcessStatusCreate, db: Session = Depends(get_db)):
    new_process_status = ProcessStatusModel(**process_status.dict())
    try:
        db.add(new_process_status)
        db.commit()
    except SQLAlchemyError:
        raise HTTPException(500, detail="An error occurred while inserting the process_status data to db")
    return {"message": "process status created"}, 200
