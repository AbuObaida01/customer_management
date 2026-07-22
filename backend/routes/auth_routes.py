from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserRegister, Token,SendOTPRequest,VerifyOTPRequest, MessageResponse
from services.otp_service import OTPService
from services.email_service import EmailService

from utils.password import hash_password, verify_password

from utils.jwt_handler import create_access_token

router = APIRouter()

@router.post("/register")
def register_user(user_dat: UserRegister, db: Session=Depends(get_db)):
    #check if user exists
    existing_user=db.query(User).filter(User.email==user_dat.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    
    new_user=User(username=user_dat.username, email=user_dat.email, password=hash_password(user_dat.password))

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return MessageResponse(message="User registered successfully")

@router.post("/login",response_model=MessageResponse)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    user = (db.query(User).filter(User.email == form_data.username).first())
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password.")
    if not verify_password(form_data.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password.")
    otp = OTPService.save_otp(db,user.email)
    email_sent = EmailService.send_otp(user.email,otp)

    if not email_sent:
        raise HTTPException(
            status_code=500,
            detail="Failed to send OTP."
        )

    return MessageResponse(message="OTP sent successfully.")

@router.post("/send-otp",response_model=MessageResponse)
def send_otp(
    request: SendOTPRequest,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(
            User.email == request.email
        )
        .first()
    )
    if user is None:
        raise HTTPException(
            status_code=400,
            detail="No account found with this email."
        )
    otp = OTPService.save_otp(
        db,
        request.email
    )
    email_sent = EmailService.send_otp(
        request.email,
        otp
    )
    if not email_sent:
        raise HTTPException(
            status_code=500,
            detail="Failed to send OTP."
        )
    return MessageResponse(message="OTP sent successfully.")

@router.post("/verify-otp", response_model=Token)
def verify_otp(
    request: VerifyOTPRequest,
    db: Session = Depends(get_db)
):
    user=(
        db.query(User)
        .filter(User.email == request.email)
        .first()
    )
    if user is None:
        raise HTTPException(
            status_code=400,
            detail="No account found with this email."
        )
    valid= OTPService.verify_otp(
        db,
        request.email,
        request.otp
    )
    if not valid:
        raise HTTPException(
            status_code=400,
            detail="Invalid or expired OTP."
        )
    access_token = create_access_token(
        {
            "sub": request.email
        }
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
