from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.user import Users
from dependencies import connect_to_db
from schemas.user import UserCreate, UserUpdate, UserResponse, UserLogin, UserPatch

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/create", response_model=UserResponse)
def create_user(user_data: UserCreate, db: Session = Depends(connect_to_db)):
    user = Users(**user_data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login", response_model=UserResponse)
def login_user(user_credentials: UserLogin, db: Session = Depends(connect_to_db)):
    user = db.query(Users).filter(Users.email == user_credentials.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.password != user_credentials.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
        
    return user


@router.get("/", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(connect_to_db)):
    return db.query(Users).all()


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(connect_to_db)):
    user = db.query(Users).filter(Users.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(connect_to_db)):
    user = db.query(Users).filter(Users.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted"}


@router.patch("/{user_id}", response_model=UserResponse)
def patch_user(
    user_id: int,
    user_data: UserPatch,
    db: Session = Depends(connect_to_db)
):
    user = db.query(Users).filter(Users.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = user_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user

