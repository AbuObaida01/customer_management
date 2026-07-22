from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Customer
from auth import get_current_user

router=APIRouter()

@router.get("/customers")
def get_customers(
    city: str |None=None,
    country: str |None=None,
    company: str |None=None,
    email: str |None=None,
    page: int=1,
    page_size: int=10,
    db: Session=Depends(get_db),
    current_user=Depends(get_current_user)
):
    query=db.query(Customer)
    if city:
        query=query.filter(Customer.city==city)
    if country:
        query=query.filter(Customer.country==country)
    if company:
        query=query.filter(Customer.company==company)
    if email:
        query=query.filter(Customer.email==email)

    total_records=query.count()
    customers=query.offset((page-1)*page_size).limit(page_size).all()
    return{
        "page":page,
        "page_size":page_size,
        "total_records":total_records,
        "returned_records":len(customers),
        "data":customers
    } 