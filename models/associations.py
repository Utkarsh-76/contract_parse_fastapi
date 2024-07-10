from sqlalchemy import Column, Integer, ForeignKey, Table
from database import Base

# Association table for the many-to-many relationship
process_ert = Table('process_ert', Base.metadata,
                    Column('process_id', Integer, ForeignKey('process.id'), primary_key=True),
                    Column('ert_id', Integer, ForeignKey('erts.id'), primary_key=True)
)

process_contract_type = (
    Table('process_contract_type', Base.metadata,
          Column('process_id', Integer, ForeignKey('process.id'), primary_key=True),
          Column('contract_type_id', Integer, ForeignKey('contract_types.id'), primary_key=True)
))