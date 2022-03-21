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