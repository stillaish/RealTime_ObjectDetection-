import cv2
import os

def augment_data(image_path):
    """
    Simple data augmentation: Flip and Grayscale.
    """
    if not os.path.exists(image_path):
        return
    
    img = cv2.imread(image_path)
    base_name = os.path.basename(image_path).split('.')[0]
    
    # Flip
    flipped = cv2.flip(img, 1)
    cv2.imwrite(f"dataset/samples/{base_name}_flipped.jpg", flipped)
    
    # Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"dataset/samples/{base_name}_gray.jpg", gray)
    
    print(f"Augmented {image_path}")

if __name__ == "__main__":
    # Example usage
    sample = "dataset/samples/bus.jpg"
    if os.path.exists(sample):
        augment_data(sample)
