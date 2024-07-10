from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(400), unique=True, nullable=False)
    first_name = Column(String(400), unique=False, nullable=True)
    last_name = Column(String(400), unique=False, nullable=True)
    phone = Column(String(20), unique=False, nullable=True)
    company_name = Column(String(400), unique=False, nullable=True)
    address = Column(String(4000), unique=False, nullable=True)
    city = Column(String(400), unique=False, nullable=True)
    state = Column(String(400), unique=False, nullable=True)
    zip_code = Column(String(10), unique=False, nullable=True)

    process = relationship("ProcessModel", back_populates="user", lazy="dynamic")
