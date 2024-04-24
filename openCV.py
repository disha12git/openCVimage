import numpy as np
import cv2

def create_image(height, width):
    # Create a black image
    image = np.zeros((height, width, 3), np.uint8)
    # Draw a white rectangle in the middle
    cv2.rectangle(image, (width//4, height//4), (3*width//4, 3*height//4), (255, 255, 255), -1)
    return image

def main():
    height = 400
    width = 600
    image = create_image(height, width)
    cv2.imshow('Output Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
