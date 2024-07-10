from pydantic import BaseModel
from typing import List


class ErtList(BaseModel):
    erts: List[int]


class ContractTypeList(BaseModel):
    contract_types: List[str]