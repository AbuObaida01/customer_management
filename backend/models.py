from datetime import datetime
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean
from database import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True, index=True)
    username=Column(String(100),nullable=False)
    email=Column(String(100), unique=True, nullable=False, index=True)
    password=Column(String(255), nullable=False)

class Customer(Base):
    __tablename__="customers"
    customer_id=Column(String(50), primary_key=True)
    first_name=Column(String(100))
    last_name=Column(String(50))
    company=Column(String(200))
    city=Column(String(100))
    country=Column(String(100))
    phone_1=Column(String(20))
    phone_2=Column(String(20))
    email=Column(String(100))
    subscription_date=Column(Date)
    website=Column(String(100))

class OTPVerification(Base):
    __tablename__="otp_verification"
    id=Column(Integer, primary_key=True,index=True)
    email=Column(String(255), nullable=False, index=True)
    otp=Column(String(255),nullable=False)
    expires_at=Column(DateTime, nullable=False)
    created_at=Column(DateTime, default=datetime.utcnow, nullable=False)
    is_used=Column(Boolean, nullable=False, default=False)