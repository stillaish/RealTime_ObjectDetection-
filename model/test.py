from ultralytics import YOLO

def test_model():
    """
    Test the model on a single image.
    """
    model = YOLO('yolov8n.pt')
    results = model('dataset/samples/bus.jpg')
    
    for result in results:
        result.show() # Display results

if __name__ == "__main__":
    test_model()
