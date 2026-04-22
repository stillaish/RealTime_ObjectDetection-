# Real-Time Object Detection Platform

A production-ready real-time object detection platform. It combines the power of **YOLOv8** with a high-performance **FastAPI** backend and a modern **React** dashboard.

## 🚀 Key Features
- **Live Stream Detection**: Capture and analyze camera frames in real-time.
- **Modern Dashboard**: Glassmorphism UI with live metrics and latency tracking.
- **Improved Accuracy**: Powered by the **YOLOv8 Medium** model for high-precision detection (Phones, Pens, Laptops, etc.).
- **Model Management**: Dedicated tools for training, testing, and evaluating models.

## 📁 Project Structure
- **frontend/**: React (Vite) application with premium styling.
- **backend/**: FastAPI server logic and AI inference engine.
- **model/**: Scripts for training (`train.py`), testing (`test.py`), and evaluation (`evaluate.py`).
- **dataset/**: Scripts for downloading and augmenting training data.
- **utils/**: Core utilities like `fps_counter.py`, `draw_boxes.py`, and `config.py`.

## 📦 Installation

### 1. Backend Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### 2. Dataset & Model Setup (Optional)
```bash
# Download sample data
python dataset/downloader.py

# Test the model
python model/test.py
```

### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

---

## 🛠️ Technology Stack
- **Frontend**: React, Lucide Icons, Axios.
- **Backend**: FastAPI, Ultralytics YOLOv8, OpenCV, Pillow.
- **Inference**: YOLOv8m (Medium) for balanced speed and accuracy.

---

## 🛡️ Original Implementation
This project is an original implementation designed for speed, modularity, and aesthetic excellence. It avoids legacy templates and focuses on modern, asynchronous web standards.
