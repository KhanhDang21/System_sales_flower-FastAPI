from configs.database import Base
from sqlalchemy import Column, Integer, String


class Bill(Base):
    __tablename__ = 'bills'

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    customer_number_phone = Column(String, nullable=False)
    customer_address = Column(String, nullable=False)
    flower_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    pay = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
