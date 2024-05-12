# test_object_detection.py
import unittest
from filter_objects import filter_objects
from sort_objects import sort_objects

class TestObjectDetection(unittest.TestCase):
    def test_filter_objects(self):
        objects = [{'size': 20, 'confidence': 0.8}, {'size': 5, 'confidence': 0.3}]
        filtered_objects = filter_objects(objects, min_size=10)
        self.assertEqual(len(filtered_objects), 1)

    def test_sort_objects(self):
        objects = [{'position': [10, 20], 'ize': 30}, {'position': [5, 10], 'ize': 20}]
        sorted_objects = sort_objects(objects, by='position')
        self.assertEqual(sorted_objects[0]['position'], [5, 10])

if __name__ == '__main__':
    unittest.main()
