from typing import List
from pydantic import BaseModel
from .base_response import BaseResponse


class Bill(BaseModel):
    id: int
    customer_name: str
    customer_number_phone: str
    customer_address: str
    flower_id: int
    quantity: int
    pay: int
    day: int
    month: int
    year: int

    class Config:
        from_attributes = True


class BillCreate(BaseModel):
    customer_name: str
    customer_number_phone: str
    customer_address: str
    flower_id: int
    quantity: int
    day: int
    month: int
    year: int


class BillResponse(BaseResponse):
    data: List[Bill] = []
    length: int = 0
