# filter_results.py
import numpy as np

def filter_results(results, min_confidence=0.5):
    """
    Filter recognition results based on their confidence score.

    Args:
        results (list): List of recognition results
        min_confidence (float, optional): Minimum confidence score of results to keep. Defaults to 0.5.

    Returns:
        list: Filtered list of recognition results
    """
    filtered_results = []
    for result in results:
        if result['confidence'] >= min_confidence:
            filtered_results.append(result)
    return filtered_results
