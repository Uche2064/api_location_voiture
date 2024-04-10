from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, db, models
from sqlalchemy.orm import Session


route = APIRouter(
    prefix="/car",
    tags=["Car"]
)


@route.get("/", response_model=List[schemas.VoitureResponse])
async def get_all_cars(db: Session = Depends(db.get_db), skip: int = 0, limit: int = 100):
    cars = db.query(models.Car).offset(skip).limit(limit).all()
    return cars



@route.post("/", response_model=schemas.VoitureResponse)
async def save_car(car: schemas.BaseVoiture, db: Session = Depends(db.get_db)):
    new_car = models.Car(**car.model_dump())
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return new_car

@route.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_car(id: int, db: Session = Depends(db.get_db)):
    car = db.query(models.Car).filter(models.Car.id == id)
    if not car.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Car not found")
    car.delete()
    db.commit()

