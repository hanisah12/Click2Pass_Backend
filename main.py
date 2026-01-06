from fastapi import FastAPI
from routers.user import router as user_router
from routers.routers_pass import router as pass_router
from routers.message import router as message_router
from db.database import Base, engine

app = FastAPI(title="Bus Pass Booking API")

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(pass_router)
app.include_router(message_router)

@app.get("/")
def root():
    return {"message": "Welcome to Bus Pass Booking API"}
