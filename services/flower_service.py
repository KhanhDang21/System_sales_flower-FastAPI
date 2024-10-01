from sqlalchemy.orm import Session
from models.flower import Flower as FlowerModel
from schemas.flower import Flower as FlowerSchema, FlowerCreate
from typing import List


def get_flower_service():
    try:
        yield FlowerService()
    finally:
        pass


class FlowerService:
    def get_all_flowers(self, db: Session) -> List[FlowerSchema]:
        return db.query(FlowerModel).all()

    def get_flower_by_id(self, flower_id: int, db: Session) -> FlowerSchema:
        return db.query(FlowerModel).filter(FlowerModel.id == flower_id).first()

    def createflower(self, flower: FlowerCreate, db: Session) -> FlowerSchema:
        new_flower = FlowerModel(**flower.dict())
        db.add(new_flower)
        db.commit()
        db.refresh(new_flower)
        return new_flower

    def update_flower(self, flower_id: int, flower_new: FlowerCreate, db: Session) -> FlowerSchema:
        flower_old = db.query(FlowerModel).filter(FlowerModel.id == flower_id).first()
        flower_old.name = flower_new.name
        flower_old.description = flower_new.description
        flower_old.price = flower_new.price
        flower_old.quantity = flower_new.quantity
        db.commit()
        db.refresh(flower_old)
        return flower_old

    def delete_flower(self, flower_id: int, db: Session):
        flower_old = db.query(FlowerModel).filter(FlowerModel.id == flower_id).first()
        db.delete(flower_old)
        db.commit()
        db.refresh(flower_old)
