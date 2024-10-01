from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from schemas.authentication import Register
from configs.database import get_db
from exceptions import raise_error

from services.authentication_service import AuthenticationService, get_authen_service

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)


@router.post("/login")
def login(login_data: OAuth2PasswordRequestForm = Depends(), authen_service=Depends(get_authen_service),
          db=Depends(get_db)):
    try:
        response = authen_service.authencate_user(login_data, db)

        if response is None:
            return raise_error(1002)

        return response
    except Exception:
        return raise_error(1001)


@router.post("/register")
def register(register_data: Register, authen_service=Depends(get_authen_service),
             db=Depends(get_db)):
    try:
        return authen_service.register_user(register_data, db)
    except Exception:
        return raise_error(1003)
