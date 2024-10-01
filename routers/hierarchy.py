from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.base_response import BaseResponse
from services.flower_service import get_flower_service
from configs.database import get_db
from configs.authentication import get_current_user
from schemas.flower import FlowerCreate, FlowerResponse
from exceptions import raise_error
from models.flower import Flower as FlowerModel
from models.customer import Customer as CustomerModel

router = APIRouter(
    prefix="/api/hierarchy",
    tags=["Hierarchy"],
)

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/{hierarchy_name}", response_model=BaseResponse)
def get_hierarchy(hierarchy: str, db: db_dependency):
    db_customer = db.query(CustomerModel).filter(CustomerModel.hierarchy == hierarchy).all()

    res = []
    for customer in db_customer:
        res.append(
            {
                "customer_name": customer.name,
                "customer_number_phone": customer.number_phone,
                "customer_address": customer.address,
                "total_pay": customer.total_pay
            }
        )
    return res
