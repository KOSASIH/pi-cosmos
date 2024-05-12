# sort_results.py
import numpy as np

def sort_results(results, by='relevance', ascending=True):
    """
    Sort recognition results based on their relevance or other attributes.

    Args:
        results (list): List of recognition results
        by (str, optional): Attribute to sort by. Defaults to 'elevance'.
        ascending (bool, optional): Sort in ascending order. Defaults to True.

    Returns:
        list: Sorted list of recognition results
    """
    if by == 'elevance':
        results.sort(key=lambda x: x['relevance'], reverse=not ascending)
    else:
        raise ValueError("Invalid sort attribute")
    return results
