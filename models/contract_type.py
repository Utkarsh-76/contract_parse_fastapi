from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base
from models.associations import process_contract_type


class ContractTypeModel(Base):
    __tablename__ = "contract_types"

    id = Column(Integer, primary_key=True)
    contract_type = Column(String(400), unique=True, nullable=False)

    process = relationship('ProcessModel', secondary=process_contract_type, back_populates="contract_types")