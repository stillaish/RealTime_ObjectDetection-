import os

# Application Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

API_HOST = "0.0.0.0"
API_PORT = 8000
MODEL_PATH = os.path.join(BASE_DIR, "yolov8m.pt")
CONFIDENCE_THRESHOLD = 0.5
DETECTION_INTERVAL_MS = 500

