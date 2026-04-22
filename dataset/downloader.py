import os
import requests

def download_sample_images():
    """
    Downloads sample images for testing object detection.
    """
    samples = {
        "bus.jpg": "https://ultralytics.com/images/bus.jpg",
        "zidane.jpg": "https://ultralytics.com/images/zidane.jpg"
    }
    
    os.makedirs("dataset/samples", exist_ok=True)
    
    for name, url in samples.items():
        path = os.path.join("dataset/samples", name)
        if not os.path.exists(path):
            print(f"Downloading {name}...")
            response = requests.get(url)
            with open(path, "wb") as f:
                f.write(response.content)
    print("Sample images ready in dataset/samples/")

if __name__ == "__main__":
    download_sample_images()
