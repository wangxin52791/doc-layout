from PIL import Image
from fastapi import FastAPI, UploadFile, File,Body
from PIL import Image
import vision.t_recognizer as recon
from PyPDF2 import PdfReader
from io import BytesIO
import pdfplumber

app = FastAPI()

@app.post("/upload_image/")
async def upload_image(file: UploadFile = File(...), threshold: float = Body(0.2)):
    image = Image.open(BytesIO(await file.read()))
    outputs=recon.main(image, output_dir="./results", threshold=threshold)
    return {"filename": file.filename, "results":outputs}

@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...), threshold: float = Body(0.2)):
    pdf = pdfplumber.open(BytesIO(await file.read()))
    outputs=recon.main(pdf, output_dir="./results", threshold=threshold)
    return {"filename": file.filename,"results":outputs}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)