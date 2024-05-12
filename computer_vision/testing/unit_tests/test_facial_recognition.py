# test_facial_recognition.py
import unittest
from filter_faces import filter_faces
from sort_faces import sort_faces

class TestFacialRecognition(unittest.TestCase):
    def test_filter_faces(self):
        faces = [{'similarity': 0.6}, {'similarity': 0.3}]
        filtered_faces = filter_faces(faces, min_similarity=0.5)
        self.assertEqual(len(filtered_faces), 1)

    def test_sort_faces(self):
        faces = [{'position': [10, 20], 'ize': 30}, {'position': [5, 10], 'ize': 20}]
        sorted_faces = sort_faces(faces, by='position')
        self.assertEqual(sorted_faces[0]['position'], [5, 10])

if __name__ == '__main__':
    unittest.main()
