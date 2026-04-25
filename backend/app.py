import cv2
import numpy as np
from ultralytics import YOLO
import base64
from PIL import Image
import io
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# Initialize FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from utils.config import MODEL_PATH, API_HOST, API_PORT

# Load YOLO Model
model = YOLO(MODEL_PATH) 
model.to('cpu') # Ensure it runs on CPU to save RAM

class FrameData(BaseModel):
    image: str # Base64 string

@app.get("/")
def home():
    return {"message": "Backend is Running"}

@app.post("/detect")
async def detect(data: FrameData):
    try:
        # Decode image
        header, encoded = data.image.split(",", 1)
        image_bytes = base64.b64decode(encoded)
        image = Image.open(io.BytesIO(image_bytes))
        
        # Convert to OpenCV format
        frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # Run YOLO
        results = model(frame)
        
        detections = []
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                label = model.names[cls]

                detections.append({
                    "label": label,
                    "confidence": round(conf, 2),
                    "bbox": [int(x1), int(y1), int(x2), int(y2)]
                })

        return {"detections": detections}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=API_HOST, port=API_PORT)
