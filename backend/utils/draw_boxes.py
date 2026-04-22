import cv2

def draw_detections(frame, detections):
    """
    Utility to draw bounding boxes and labels on an OpenCV frame.
    """
    for det in detections:
        x1, y1, x2, y2 = det['bbox']
        label = f"{det['label']} {det['confidence']}"
        
        # Draw Box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # Draw Label
        cv2.putText(frame, label, (x1, y1 - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    return frame
