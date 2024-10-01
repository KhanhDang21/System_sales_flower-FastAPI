from pydantic import BaseModel


class Register(BaseModel):
    username: str
    password: str
    role: str = 'user'


class Token(BaseModel):
    access_token: str
    token_type: str = 'Bearer'


class TokenData(BaseModel):
    username: str = None
    role: str = None
