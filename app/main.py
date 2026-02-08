from fastapi import FastAPI, UploadFile, File

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    return {"message": "file received"}
