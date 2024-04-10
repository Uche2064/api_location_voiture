from datetime import datetime
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, db, models, oauth2
from sqlalchemy.orm import Session


route = APIRouter(
    prefix="/car",
    tags=["Car"]
)


@route.get("/", response_model=List[schemas.VoitureResponse])
async def get_all_cars(db: Session = Depends(db.get_db), skip: int = 0, limit: int = 100, search: Optional[str] = "", current_user: int = Depends(oauth2.get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=401, detail="Authentification a échoué")
    cars = db.query(models.Car).filter(models.Car.marque.contains(search)).offset(skip).limit(limit).all()
    if cars is None:
        return "No cars"
    return cars


@route.post("/", response_model=schemas.VoitureResponse)
async def save_car(car: schemas.BaseVoiture, db: Session = Depends(db.get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_car = models.Car(**car.model_dump())
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return new_car


@route.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_car(id: int, db: Session = Depends(db.get_db), current_user: int = Depends(oauth2.get_current_user)):
    car = db.query(models.Car).filter(models.Car.id == id)
    if not car.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Voiture non trouvé")
    car.delete(synchronize_session=False)
    db.commit()

@route.put("/{id}", response_model=schemas.VoitureResponse)
async def update_car(id: int, car: schemas.UpdateCar, db: Session = Depends(db.get_db), current_user: int = Depends(oauth2.get_current_user)):
    get_car = db.query(models.Car).filter(models.Car.id == id)
    if get_car.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Voiture non trouvé")
    car.updated_at = datetime.now()

    get_car.update(car.model_dump(exclude_none=True), synchronize_session=False)
    db.commit()
    return get_car.first()