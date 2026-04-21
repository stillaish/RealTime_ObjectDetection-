import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import Camera from './components/Camera';
import './App.css';

function App() {
  const [detections, setDetections] = useState([]);
  const [latency, setLatency] = useState(0);
  const isProcessing = useRef(false);

  useEffect(() => {
    const interval = setInterval(async () => {
      if (isProcessing.current) return;

      const video = document.querySelector('video');
      if (!video || video.readyState !== 4) return;

      // Capture frame
      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      const frame = canvas.toDataURL('image/jpeg', 0.6);

      try {
        isProcessing.current = true;
        const start = Date.now();
        const response = await axios.post('http://localhost:8000/detect', { image: frame });
        setLatency(Date.now() - start);
        setDetections(response.data.detections || []);
      } catch (err) {
        console.error("API error:", err);
      } finally {
        isProcessing.current = false;
      }
    }, 500);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="app-container">
      <header>
        <h1>Real-Time Object Detection</h1>
        <div>Latency: {latency}ms</div>
      </header>

      <div className="main-layout">
        <Camera detections={detections} />
        
        <div className="stats-panel">
          <h3>Detections</h3>
          <div className="stat-card">
            <div className="stat-number">{detections.length}</div>
            <div>Objects Found</div>
          </div>
          
          <div className="detection-list">
            {detections.map((det, i) => (
              <div key={i} className="detection-item">
                <span className="label">{det.label}</span>
                <span>{Math.round(det.confidence * 100)}%</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
