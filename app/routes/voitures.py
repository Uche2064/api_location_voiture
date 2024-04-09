from fastapi import APIRouter

route = APIRouter(
    prefix="/voitures",
    tags=["Voitures"],
)

@route.get("/")
def get_voiture():
    return {"data": "Voitures"}