from fastapi import FastAPI, Request
from .config import setting
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

@app.middleware("http")
async def update_access_token_expire(request: Request, call_next):
    response = await call_next(request)
    setting.expiration_time+=5
    return response

app.include_router(user.route)
app.include_router(car.route)
app.include_router(auth.route)




