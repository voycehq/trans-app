from pydantic import BaseModel, Field


class SignupDTO(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=20)
    email: str = Field(...)
    password: str = Field(..., min_length=8)

    class Config:
        orm_mode = True


class EmailVerificationDTO(BaseModel):
    code: str
    email: str

    class Config:
        orm_mode = True


class LoginDTO(BaseModel):
    email: str = Field(..., title='Your account email')
    password: str = Field(..., title='Your account password')

    class Config:
        orm_mode = True


class ResendVerificationCodeDTO(BaseModel):
    email: str = Field(..., title='Your account email')

    class Config:
        orm_mode = True


class ResetPasswordDTO(BaseModel):
    email: str = Field(..., title='Your account email')
    code: str = Field(..., min_length=9)
    password: str = Field(..., min_length=8)

    class Config:
        orm_mode = True
