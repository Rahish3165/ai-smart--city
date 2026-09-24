import os
import json
import random
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.json")

@app.get("/api/heatmap-data")
def get_heatmap_data():
    try:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return {
            "incidents": data,
            "predictions": []
        }
    except FileNotFoundError:
        return {"incidents": [], "predictions": []}

@app.post("/api/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "ai_analysis": random.choice(["pothole", "garbage", "leak", "crack"]),
        "confidence": round(random.uniform(70.0, 99.9), 2),
        "alert_triggered": random.random() > 0.5
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
