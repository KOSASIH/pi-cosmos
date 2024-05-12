# cosmos.py
from typing import List
from .utils import get_logger

logger = get_logger(__name__)

class Cosmos:
    def __init__(self, data: List[dict]):
        self.data = data

    def get_stars(self) -> List[dict]:
        """Return a list of stars"""
        return [star for star in self.data if star['type'] == 'star']

    def get_planets(self) -> List[dict]:
        """Return a list of planets"""
        return [planet for planet in self.data if planet['type'] == 'planet']
