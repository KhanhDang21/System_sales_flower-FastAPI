from typing import List
from pydantic import BaseModel
from .base_response import BaseResponse


class Flower(BaseModel):
    id: int
    name: str
    description: str = ''
    price: int
    quantity: int

    class Config:
        from_attributes = True


class FlowerCreate(BaseModel):
    name: str
    description: str = ''
    price: int
    quantity: int


class FlowerResponse(BaseResponse):
    data: List[Flower] = []
    length: int = 0
