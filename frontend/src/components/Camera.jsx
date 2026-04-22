import React, { useRef, useEffect } from 'react';

const Camera = ({ detections }) => {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);

  useEffect(() => {
    async function startCamera() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        videoRef.current.srcObject = stream;
      } catch (err) {
        console.error("Camera error:", err);
      }
    }
    startCamera();
  }, []);

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const video = videoRef.current;

    if (!video || !canvas) return;

    // Match canvas size to video
    canvas.width = video.videoWidth || 640;
    canvas.height = video.videoHeight || 480;

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    detections.forEach(det => {
      const [x1, y1, x2, y2] = det.bbox;
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 4;
      ctx.strokeRect(x1, y1, x2 - x1, y2 - y1);

      ctx.fillStyle = '#38bdf8';
      ctx.font = '16px Inter';
      ctx.fillText(`${det.label} ${Math.round(det.confidence * 100)}%`, x1, y1 > 20 ? y1 - 10 : y1 + 20);
    });
  }, [detections]);

  return (
    <div className="camera-box">
      <video ref={videoRef} autoPlay playsInline muted />
      <canvas ref={canvasRef} />
    </div>
  );
};

export default Camera;
