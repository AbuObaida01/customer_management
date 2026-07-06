from fastapi import FastAPI
from routes.auth_routes import router as auth_router
from database import Base
from database import engine
from fastapi.middleware.cors import CORSMiddleware

from routes.customers_routes import router as customers_router
app=FastAPI(title="Customer Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
app.include_router(auth_router)
app.include_router(customers_router)
@app.get("/")
def home():
    return {"message": "Hello, World!"}
