# filter_faces.py
import numpy as np

def filter_faces(faces, min_similarity=0.5):
    """
    Filter recognized faces based on their similarity score.

    Args:
        faces (list): List of recognized faces
        min_similarity (float, optional): Minimum similarity score of faces to keep. Defaults to 0.5.

    Returns:
        list: Filtered list of recognized faces
    """
    filtered_faces = []
    for face in faces:
        if face['similarity'] >= min_similarity:
            filtered_faces.append(face)
    return filtered_faces
