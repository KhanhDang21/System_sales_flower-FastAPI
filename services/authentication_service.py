from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from schemas.authentication import Register
from schemas.user import User as UserSchema
from models.user import User as UserModel
from schemas.authentication import TokenData, Token
from configs.authentication import verify_password, get_password_hash, create_access_token


def get_authen_service():
    try:
        yield AuthenticationService()
    finally:
        pass


class AuthenticationService:
    def authencate_user(self, login_data: OAuth2PasswordRequestForm, db: Session) -> Token:
        user = db.query(UserModel).filter(UserModel.username == login_data.username).first()
        if not user:
            return None
        if not verify_password(login_data.password, user.password):
            return None

        access_token = create_access_token(data={"username": user.username, 'role': user.role})

        return Token(access_token=access_token)

    def register_user(self, register_data: Register, db: Session) -> UserSchema:
        new_user = UserModel(
            username=register_data.username,
            password=get_password_hash(register_data.password),
            role=register_data.role
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return UserSchema(
            id=new_user.id,
            username=new_user.username,
            role=new_user.role
        )
