import cv2
import numpy as np
from random import randint

def augment_image(image):
    """
    Augments an input image with random transformations.

    Args:
        image (numpy.ndarray): Input image.

    Returns:
        numpy.ndarray: Augmented image.
    """
    # Randomly flip the image horizontally
    if randint(0, 1) == 1:
        image = cv2.flip(image, 1)

    # Randomly rotate the image
    rows, cols, _ = image.shape
    center = (cols / 2, rows / 2)
    M = cv2.getRotationMatrix2D(center, randint(-10, 10), 1.0)
    image = cv2.warpAffine(image, M, (cols, rows))

    # Randomly brighten the image
    image = cv2.addWeighted(image, 1, np.zeros(image.shape, image.dtype), 0, randint(-20, 20) / 100.0)

    return image
