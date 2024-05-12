# utils.py
import logging

def get_logger(name: str) -> logging.Logger:
    """Return a logger instance with the given name"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger

def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate the distance between two points on a sphere"""
    # implementation remains the same
    pass
