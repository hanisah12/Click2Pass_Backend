from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.apply_pass import ApplyPass
from dependencies import connect_to_db
from schemas.passes import PassCreate, PassUpdate, PassResponse

router = APIRouter(prefix="/passes", tags=["Passes"])

@router.post("/create", response_model=PassResponse)
def create_pass(pass_data: PassCreate, db: Session = Depends(connect_to_db)):
    new_pass = ApplyPass(**pass_data.model_dump())
    db.add(new_pass)
    db.commit()
    db.refresh(new_pass)
    return new_pass
    

@router.get("/", response_model=list[PassResponse])
def get_all_passes(db: Session = Depends(connect_to_db)):
    return db.query(ApplyPass).all()

@router.get("/user/{user_id}", response_model=list[PassResponse])
def get_user_passes(user_id: int, db: Session = Depends(connect_to_db)):
    return db.query(ApplyPass).filter(ApplyPass.user_id == user_id).all()

@router.get("/{pass_id}", response_model=PassResponse)
def get_pass(pass_id: int, db: Session = Depends(connect_to_db)):
    bus_pass = db.query(ApplyPass).filter(ApplyPass.pass_id == pass_id).first()
    if not bus_pass:
        raise HTTPException(status_code=404, detail="Pass not found")
    return bus_pass


@router.put("/{pass_id}", response_model=PassResponse)
def renew_pass(pass_id: int,pass_data: PassUpdate,db: Session = Depends(connect_to_db)):
    bus_pass = db.query(ApplyPass).filter(ApplyPass.pass_id == pass_id).first()
    if not bus_pass:
        raise HTTPException(status_code=404, detail="Pass not found")

    for key, value in pass_data.model_dump().items():
        setattr(bus_pass, key, value)

    db.commit()
    db.refresh(bus_pass)
    return bus_pass

@router.delete("/{pass_id}")
def delete_pass(pass_id: int, db: Session = Depends(connect_to_db)):
    bus_pass = db.query(ApplyPass).filter(ApplyPass.pass_id == pass_id).first()
    if not bus_pass:
        raise HTTPException(status_code=404, detail="Pass not found")

    db.delete(bus_pass)
    db.commit()
    return {"message": "Pass deleted"}





 



