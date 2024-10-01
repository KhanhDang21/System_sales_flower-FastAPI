from fastapi import APIRouter, Depends
from schemas.base_response import BaseResponse
from services.flower_service import get_flower_service
from configs.database import get_db
from configs.authentication import get_current_user
from schemas.flower import FlowerCreate, FlowerResponse
from exceptions import raise_error
from models.flower import Flower as FlowerModel

router = APIRouter(
    prefix="/api/flowers",
    tags=["Flowers"],
)


@router.get("", response_model=FlowerResponse | BaseResponse)
def get_all_flowers(flower_service=Depends(get_flower_service), db=Depends(get_db), user=Depends(get_current_user)):
    try:
        flowers = flower_service.get_all_flowers(db)
        return FlowerResponse(
            data=flowers,
            length=len(flowers)
        )
    except Exception:
        return raise_error(2001)


@router.get("/{id}", response_model=FlowerResponse | BaseResponse)
def get_flower_by_id(flower_id: int, flower_service=Depends(get_flower_service), db=Depends(get_db),
                     user=Depends(get_current_user)):
    try:
        flower = flower_service.get_flower_by_id(flower_id, db)
        return FlowerResponse(
            data=[flower],
            length=1
        )
    except Exception:
        return raise_error(2001)


@router.post("", response_model=FlowerResponse)
def create_flower(flower: FlowerCreate, flower_service=Depends(get_flower_service), db=Depends(get_db),
                  user=Depends(get_current_user)):
    try:
        if user.role != "admin":
            return FlowerResponse(
                message="You are not authorized to create a flower",
                status="error"
            )

        return FlowerResponse(
            data=[flower_service.createflower(flower, db)],
            length=1
        )
    except Exception:
        return raise_error(2002)


@router.put("/{id}", response_model=FlowerResponse | BaseResponse)
def update_flower(flower_id: int, flower_new: FlowerCreate, flower_service=Depends(get_flower_service),
                  db=Depends(get_db),
                  user=Depends(get_current_user)):
    try:
        if user.role != "admin":
            return FlowerResponse(
                message="You are not authorized to update a flower",
                status="error"
            )
        return FlowerResponse(
            data=[flower_service.update_flower(flower_id, flower_new, db)],
            length=1
        )
    except Exception:
        return raise_error(2003)


@router.delete("/{id}", response_model=FlowerResponse | BaseResponse)
def delete_flower(flower_id: int, flower_service=Depends(get_flower_service), db=Depends(get_db),
                  user=Depends(get_current_user)):
    if user.role != "admin":
        return FlowerResponse(
            message="You are not authorized to delete a flower",
            status="error"
        )
    flower = db.query(FlowerModel).filter(FlowerModel.id == flower_id).first()
    if flower is None:
        return raise_error(2004)
    flower_service.delete_flower(flower_id, db)