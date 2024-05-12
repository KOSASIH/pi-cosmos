# test_facial_recognition_pipeline.py
import unittest
from facial_recognition import recognize_faces
from filter_faces import filter_faces
from sort_faces import sort_faces

class TestFacialRecognitionPipeline(unittest.TestCase):
    def test_pipeline(self):
        image = np.random.rand(100, 100, 3)
        faces = recognize_faces(image)
        filtered_faces = filter_faces(faces, min_similarity=0.5)
        sorted_faces = sort_faces(filtered_faces, by='position')
        self.assertEqual(len(sorted_faces), 1)

if __name__ == '__main__':
    unittest.main()
