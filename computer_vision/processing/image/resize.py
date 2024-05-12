import cv2
import numpy as np

def resize_image(image, size=(224, 224)):
    """
    Resizes an input image to a fixed size.

    Args:
        image (numpy.ndarray): Input image.
        size (tuple): Tuple representing the desired height and width of the output image.

    Returns:
        numpy.ndarray: Resized image.
    """
    return cv2.resize(image, size, interpolation=cv2.INTER_AREA)
