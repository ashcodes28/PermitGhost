from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Permit
from schemas import PermitCreate, PermitResponse

router = APIRouter()


@router.get("/permits", response_model=list[PermitResponse])
def get_permits(db: Session = Depends(get_db)):
    return db.query(Permit).all()


@router.post("/permits", response_model=PermitResponse)
def create_permit(permit: PermitCreate, db: Session = Depends(get_db)):
    new_permit = Permit(
        permit_type=permit.permit_type,
        zone=permit.zone
    )

    db.add(new_permit)
    db.commit()
    db.refresh(new_permit)

    return new_permit

from models import Sensor
from schemas import SensorResponse


@router.get("/sensors", response_model=list[SensorResponse])
def get_sensors(db: Session = Depends(get_db)):
    return db.query(Sensor).all()