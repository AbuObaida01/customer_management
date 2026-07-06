from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserRegister, Token

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

    return {"message": "User registered successfully"}

#User Login
# @router.post("/login", response_model=Token)
# def login_user(user_data:UserLogin,
#                db:Session=Depends(get_db)):
#     user=db.query(User).filter(User.email==user_data.email).first()
#     if user is None:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
#     if not verify_password(user_data.password, user.password):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
#     access_token=create_access_token(data={"sub": user.email})
#     return {"access_token": access_token, "token_type": "bearer"}


@router.post(
    "/login",
    response_model=Token
)
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(
            User.email == form_data.username
        )
        .first()
    )

    if user is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    if not verify_password(
        form_data.password,
        user.password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    access_token = create_access_token(
        {
            "sub": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }