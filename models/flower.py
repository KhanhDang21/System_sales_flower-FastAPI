from configs.database import Base
from sqlalchemy import Column, Integer, String


class Flower(Base):
    __tablename__ = 'flowers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(10000), nullable=True)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)

