from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from schemas.process import ProcessCreate
from schemas.others import ErtList, ContractTypeList
from models.process import ProcessModel
from models.ert import ErtModel
from models.contract_type import ContractTypeModel
from database import get_db
from services.samples import get_sample_counts

router = APIRouter()


@router.post("/create/")
async def create_process(process: ProcessCreate, db: Session = Depends(get_db)):
    new_process = ProcessModel(**process.dict())
    ert_list = [ErtModel(ert=ert_no) for ert_no in process.erts]
    ct_list = [ContractTypeModel(contract_type=ct) for ct in process.contract_types]
    try:
        new_process.erts.extend(ert_list)
        new_process.contract_types.extend(ct_list)
        db.add(new_process)
        db.commit()
    except SQLAlchemyError:
        raise HTTPException(500, detail="An error occurred while adding new process data to db")
    return {"message": "process created"}, 200


@router.post("/get_samples/")
async def get_samples(erts: ErtList, contract_types: ContractTypeList):
    sample_counts = get_sample_counts(erts, contract_types)
    return sample_counts, 200
