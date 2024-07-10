from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from schemas.user import UserCreate
from models.user import UserModel
from database import get_db

router = APIRouter()


@router.post("/create/")
# @router.post("/create/", response_model=UserRead)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # db_user = db.query(User).filter(User.email == user.email).first()
    # if db_user:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    new_user = UserModel(email=user.email)
    try:
        db.add(new_user)
        db.commit()
    except SQLAlchemyError:
        raise HTTPException(500, detail="An error occurred while inserting the user to db.")
    return {"message": "user created"}, 200
