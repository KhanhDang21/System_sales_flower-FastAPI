from fastapi import APIRouter, Depends
from schemas.base_response import BaseResponse
from services.bill_services import get_bill_service
from configs.database import get_db
from configs.authentication import get_current_user
from schemas.bill import BillCreate, BillResponse
from exceptions import raise_error
from models.bill import Bill as BillModel


router = APIRouter(
    prefix="/api/bills",
    tags=["Bills"],
)


@router.get("", response_model=BillResponse | BaseResponse)
def get_all_bills(bill_service=Depends(get_bill_service), db=Depends(get_db), user=Depends(get_current_user)):
    try:
        if user.role != "admin":
            return BillResponse(
                message="You are not authorized to get all bill",
                status="error"
            )
        bills = bill_service.get_all_bills(db)
        return BillResponse(
            data=bills,
            length=len(bills)
        )
    except Exception as e:
        print(e)
        return raise_error(3001)


@router.get("/{id}", response_model=BillResponse | BaseResponse)
def get_bill_by_id(bill_id: int, bill_service=Depends(get_bill_service), db=Depends(get_db), user=Depends(get_current_user)):
    try:
        bill = bill_service.get_bill_by_id(bill_id, db)
        return BillResponse(
            data=[bill],
            length=1
        )
    except Exception:
        return raise_error(3001)


@router.post("", response_model=BillResponse)
def create_bill(bill: BillCreate, bill_service=Depends(get_bill_service), db=Depends(get_db),
                user=Depends(get_current_user)):
    try:
        if user.role != "admin":
            return BillResponse(
                message="You are not authorized to create a bill",
                status="error"
            )
        return BillResponse(
            data=[bill_service.createbill(bill, db)],
            length=1
        )
    except Exception as e:
        print(e)
        return raise_error(3002)


@router.put("/{id}", response_model=BillResponse | BaseResponse)
def update_bill(bill_id: int, bill_new: BillCreate, bill_service=Depends(get_bill_service),
                db=Depends(get_db),
                user=Depends(get_current_user)):
    try:
        if user.role != "admin":
            return BillResponse(
                message="You are not authorized to update a bill",
                status="error"
            )

        return BillResponse(
            data=[bill_service.update_bill(bill_id, bill_new, db)],
            length=1
        )
    except Exception:
        return raise_error(3003)


@router.delete("/{id}", response_model=BillResponse | BaseResponse)
def delete_bill(bill_id: int, bill_service=Depends(get_bill_service), db=Depends(get_db), user=Depends(get_current_user)):
    if user.role != "admin":
        return BillResponse(
            message="You are not authorized to delete a bill",
            status="error"
        )
    flower = db.query(BillModel).filter(BillModel.id == bill_id).first()
    if flower is None:
        return raise_error(2004)
    bill_service.delete_bill(bill_id, db)