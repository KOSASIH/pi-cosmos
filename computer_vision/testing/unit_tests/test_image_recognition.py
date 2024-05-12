# test_image_recognition.py
import unittest
from filter_results import filter_results
from sort_results import sort_results

class TestImageRecognition(unittest.TestCase):
    def test_filter_results(self):
        results = [{'confidence': 0.7}, {'confidence': 0.2}]
        filtered_results = filter_results(results, min_confidence=0.5)
        self.assertEqual(len(filtered_results), 1)

    def test_sort_results(self):
        results = [{'relevance': 0.8}, {'relevance': 0.5}]
        sorted_results = sort_results(results, by='relevance')
        self.assertEqual(sorted_results[0]['relevance'], 0.8)

if __name__ == '__main__':
    unittest.main()
