from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from src.backend.model.predict import load_model, load_index_to_label_map, predict_image
from PIL import Image
from io import BytesIO
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
model = load_model()
index_to_label = load_index_to_label_map()

# Attach CORS middleware with appropriate settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(BytesIO(contents))
        result = predict_image(image, model, index_to_label)
        return JSONResponse(content={"prediction": result})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})

