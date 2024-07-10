from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from database import Base


class PaymentModel(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    status = Column(String(40), unique=False, nullable=False)
    update_date = Column(DateTime, unique=False, nullable=False)
    amount = Column(Numeric(10), unique=False, nullable=False)
    type = Column(String(40), unique=False, nullable=False)

    process_id = Column(Integer, ForeignKey('process.id'), unique=False, nullable=False)
    process = relationship("ProcessModel", back_populates="payment")
