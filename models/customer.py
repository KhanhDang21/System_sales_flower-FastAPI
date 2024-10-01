from configs.database import Base
from sqlalchemy import Column, Integer, String

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(1000), nullable=False)
    number_phone = Column(String(1000), nullable=False)
    address = Column(String(1000), nullable=False)
    total_pay = Column(Integer, nullable=False)
    hierarchy = Column(String(1000), nullable=False)
