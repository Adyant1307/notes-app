from pydantic import BaseModel, EmailStr, Field
class UserCreate(BaseModel):
    user_name: str = Field(min_length=2, max_length=64)
    user_email: EmailStr
    password: str = Field(min_length=6, max_length=128)

class UserLogin(BaseModel):
    user_email: EmailStr
    password: str

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"