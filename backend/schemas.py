from pydantic import BaseModel, EmailStr, ConfigDict, Field

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password:str

# class UserLogin(BaseModel):
#     email: EmailStr
#     password:str

class Token(BaseModel):
    access_token: str
    token_type: str

class CustomerBase(BaseModel):
    customer_id:str
    first_name:str
    last_name:str
    company:str
    city:str
    country:str
    phone_1:str
    phone_2:str
    email:EmailStr
    subscription_date:str
    website:str

    model_config=ConfigDict(
        from_attributes=True
    )

class SendOTPRequest(BaseModel):
    email: EmailStr

class VerifyOTPRequest(BaseModel):
    email: EmailStr
    otp: str=Field(
        min_length=6,
        max_length=6,
        pattern=r'^\d{6}$'
    )

class MessageResponse(BaseModel):
    message: str