from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class ProcessStatusModel(Base):
    __tablename__ = "process_status"

    id = Column(Integer, primary_key=True)
    process_start = Column(DateTime, unique=False, nullable=False)
    process_end = Column(DateTime, unique=False, nullable=False)
    current_status = Column(String(40), unique=False, nullable=False)

    process_id = Column(Integer, ForeignKey('process.id'), unique=False, nullable=False)
    process = relationship("ProcessModel", back_populates="process_status")