# filter_objects.py
import numpy as np

def filter_objects(objects, min_confidence=0.5, min_area=100):
    """
    Filters detected objects based on their confidence score and area.

    Args:
        objects (list): List of detected objects, where each object is a dictionary containing 'confidence', 'x', 'y', 'w', and 'h' keys.
        min_confidence (float): Minimum confidence score for an object to be considered valid.
        min_area (int): Minimum area for an object to be considered valid.

    Returns:
        list: List of filtered objects.
    """
    filtered_objects = []
    for obj in objects:
        if obj['confidence'] >= min_confidence and obj['w'] * obj['h'] >= min_area:
            filtered_objects.append(obj)
    return filtered_objects

# sort_objects.py
def sort_objects(objects, sort_by='confidence', reverse=True):
    """
    Sorts detected objects based on a specified attribute.

    Args:
        objects (list): List of detected objects, where each object is a dictionary containing 'confidence', 'x', 'y', 'w', and 'h' keys.
        sort_by (str): Attribute to sort objects by. Can be 'confidence', 'x', 'y', 'w', or 'h'.
        reverse (bool): Whether to sort objects in descending order.

    Returns:
        list: List of sorted objects.
    """
    if sort_by not in ['confidence', 'x', 'y', 'w', 'h']:
        raise ValueError("Invalid sort_by attribute. Must be one of 'confidence', 'x', 'y', 'w', or 'h'.")

    objects = sorted(objects, key=lambda x: x[sort_by], reverse=reverse)
    return objects
