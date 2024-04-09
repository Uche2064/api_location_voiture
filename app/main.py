from fastapi import FastAPI
import uvicorn
from routes import voitures

app = FastAPI()

app.include_router(voitures.route)




if __name__ == "__main__":
    uvicorn.run("main:app", host="127.172.0.1", port=5000, reload=True)



