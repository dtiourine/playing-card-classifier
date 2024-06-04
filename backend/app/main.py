from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from backend.model.predict import load_model, load_index_to_label_map, predict_image
import torch
from torchvision import transforms
import json
from PIL import Image
import io
from io import BytesIO

app = FastAPI()
model = load_model()
index_to_label = load_index_to_label_map()
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(BytesIO(contents))
        result = predict_image(image, model, index_to_label)
        return JSONResponse(content={"prediction": result})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})

# Retrieve target to class mapping
with open('backend/model/saved_model/target_to_class.json', 'r') as file:
    target_to_class = json.load(file)

