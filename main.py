from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
import shutil
import os
import uuid
from fastapi.middleware.cors import CORSMiddleware
from analyzer import analizar_cana

app = FastAPI()
UPLOAD_DIR = "xdxd"
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analizar")
async def analizar(file: UploadFile = File(...)):
    ext = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    filepath = os.path.join(UPLOAD_DIR, filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        data = analizar_cana(filepath)
        return JSONResponse(content=data)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.get("/imagen/{filename}")
def get_image(filename: str):
    path = os.path.join("output", filename)
    if os.path.exists(path):
        return FileResponse(path)
    return JSONResponse(content={"error": "Imagen no encontrada"}, status_code=404)
