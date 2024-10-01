from configs.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Table


class FlowerBill(Base):
    __tablename__ = 'flower_bill'

    id = Column(Integer, primary_key=True, index=True)
    flower_id = Column(Integer, ForeignKey('flowers.id'), nullable=False)
    bill_id = Column(Integer, ForeignKey('bills.id'), nullable=False)