from pydantic import BaseModel, EmailStr, ConfigDict

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