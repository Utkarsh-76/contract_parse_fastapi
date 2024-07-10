from sqlalchemy import Column, Integer, Numeric
from sqlalchemy.orm import relationship

from database import Base
from models.associations import process_ert


class ErtModel(Base):
    __tablename__ = "erts"

    id = Column(Integer, primary_key=True)
    ert = Column(Numeric(10), unique=True, nullable=False)

    process = relationship('ProcessModel', secondary=process_ert, back_populates="erts")