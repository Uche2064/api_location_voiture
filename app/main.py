from fastapi import FastAPI
import uvicorn
from app.routes import user, car, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://localhost:8000"
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user.route)
app.include_router(car.route)
app.include_router(auth.route)




