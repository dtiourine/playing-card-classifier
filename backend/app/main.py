from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from backend.model.predict import make_prediction

app = FastAPI()

origins = [
    "http://localhost:8000",  # URL of the frontend
    "http://localhost:5000",  # Adjust to actual frontend URL during deployment
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    result = await make_prediction(file)
    return {"prediction": result}

