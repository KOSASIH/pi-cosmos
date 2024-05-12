# sort_faces.py
import numpy as np

def sort_faces(faces, by='position', ascending=True):
    """
    Sort recognized faces based on their position, size, or other attributes.

    Args:
        faces (list): List of recognized faces
        by (str, optional): Attribute to sort by. Defaults to 'position'.
        ascending (bool, optional): Sort in ascending order. Defaults to True.

    Returns:
        list: Sorted list of recognized faces
    """
    if by == 'position':
        faces.sort(key=lambda x: x['position'][0], reverse=not ascending)
    elif by == 'ize':
        faces.sort(key=lambda x: x['size'], reverse=not ascending)
    else:
        raise ValueError("Invalid sort attribute")
    return faces
