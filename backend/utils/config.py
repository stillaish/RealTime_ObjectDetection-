import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

API_HOST = "0.0.0.0"
API_PORT = int(os.environ.get("PORT", 8000))
MODEL_PATH = os.path.join(BASE_DIR, "yolov8n.pt") # Switched to Nano for memory efficiency
CONFIDENCE_THRESHOLD = 0.5
DETECTION_INTERVAL_MS = 500

