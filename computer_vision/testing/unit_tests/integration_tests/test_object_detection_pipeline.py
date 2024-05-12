# test_object_detection_pipeline.py
import unittest
from object_detection import detect_objects
from filter_objects import filter_objects
from sort_objects import sort_objects

class TestObjectDetectionPipeline(unittest.TestCase):
    def test_pipeline(self):
        image = np.random.rand(100, 100, 3)
        objects = detect_objects(image)
        filtered_objects = filter_objects(objects, min_size=10)
        sorted_objects = sort_objects(filtered_objects, by='position')
        self.assertEqual(len(sorted_objects), 1)

if __name__ == '__main__':
    unittest.main()
