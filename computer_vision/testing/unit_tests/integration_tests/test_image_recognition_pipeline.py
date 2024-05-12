# test_image_recognition_pipeline.py
import unittest
from image_recognition import recognize_image
from filter_results import filter_results
from sort_results import sort_results

class TestImageRecognitionPipeline(unittest.TestCase):
    def test_pipeline(self):
        image = np.random.rand(100, 100, 3)
        results = recognize_image(image)
        filtered_results = filter_results(results, min_confidence=0.5)
        sorted_results = sort_results(filtered_results, by='relevance')
        self.assertEqual(len(sorted_results), 1)

if __name__ == '__main__':
    unittest.main()
