from sqlalchemy.orm import Session
from models.bill import Bill as BillModel
from schemas.bill import Bill as BillSchema, BillCreate
from typing import List
from models.flower import Flower
from models.customer import Customer as CustomerModel


def get_bill_service():
    try:
        yield BillService()
    finally:
        pass


def Hierarchy(total: int):
    if total <= 100000:
        return 1
    elif total > 100000 and total <= 500000:
        return 2
    elif total > 500000 and total <= 1000000:
        return 3
    elif total > 1000000:
        return 4


class BillService:
    def get_all_bills(self, db: Session) -> List[BillSchema]:
        return db.query(BillModel).all()

    def get_bill_by_id(self, bill_id: int, db: Session) -> BillSchema:
        return db.query(BillModel).filter(BillModel.id == bill_id).first()

    def createbill(self, bill: BillCreate, db: Session) -> BillSchema:
        flower = db.query(Flower).filter(Flower.id == bill.flower_id).first()
        new_bill = BillModel(
            customer_name=bill.customer_name,
            customer_number_phone=bill.customer_number_phone,
            customer_address=bill.customer_address,
            flower_id=bill.flower_id,
            quantity=bill.quantity,
            pay=bill.quantity * flower.price,
            day=bill.day,
            month=bill.month,
            year=bill.year
        )
        db.add(new_bill)
        db.commit()
        db.refresh(new_bill)
        return new_bill

    def update_bill(self, bill_id: int, bill_new: BillCreate, db: Session) -> BillSchema:
        bill_old = db.query(BillModel).filter(BillModel.id == bill_id).first()
        flower_bill_new = db.query(Flower).filter(Flower.id == bill_new.flower_id).first()
        bill_old.customer_name = bill_new.customer_name
        bill_old.customer_number_phone = bill_new.customer_number_phone
        bill_old.customer_address = bill_new.customer_address
        bill_old.flower_id = bill_new.flower_id
        bill_old.quantity = bill_new.quantity
        bill_old.pay = flower_bill_new.price * bill_new.quantity
        bill_old.day = bill_new.day
        bill_old.month = bill_new.month
        bill_old.year = bill_new.year
        db.commit()
        db.refresh(bill_old)
        return bill_old

    def delete_bill(self, bill_id: int, db: Session):
        bill_old = db.query(BillModel).filter(BillModel.id == bill_id).first()
        db.delete(bill_old)
        db.commit()
        db.refresh(bill_old)
