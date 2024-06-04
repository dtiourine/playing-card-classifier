from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/test")
async def test():
    return JSONResponse(content={"message": "Test endpoint"})
