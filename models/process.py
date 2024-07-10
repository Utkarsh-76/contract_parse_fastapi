from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base
from models.associations import process_ert, process_contract_type


class ProcessModel(Base):
    __tablename__ = "process"

    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime, unique=False, nullable=False)
    end_date = Column(DateTime, unique=False, nullable=False)
    last_update_date = Column(DateTime, unique=False, nullable=False)
    next_update_date = Column(DateTime, unique=False, nullable=False)
    frequency = Column(String(10), unique=False, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), unique=False, nullable=False)
    user = relationship("UserModel", back_populates="process")

    payment = relationship("PaymentModel", back_populates="process", lazy="dynamic")
    process_status = relationship("ProcessStatusModel", back_populates="process", lazy="dynamic")

    erts = relationship('ErtModel', secondary=process_ert, back_populates="process")
    contract_types = relationship('ContractTypeModel', secondary=process_contract_type, back_populates="process")