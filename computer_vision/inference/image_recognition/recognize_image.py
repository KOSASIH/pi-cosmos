import cv2
import numpy as np
from image_recognition.models import ImageRecognitionModel

def recognize_image(model_name, image_path):
    """
    Recognize the content of an input image using an image recognition model.

    Args:
        model_name (str): Name of the image recognition model to be used.
        image_path (str): Path to the input image file.

    Returns:
        str: Recognized content of the input image.
    """
    model = ImageRecognitionModel(model_name)
    image = cv2.imread(image_path)
    recognized_content = model.recognize(image)
    return recognized_content
