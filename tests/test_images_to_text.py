import unittest
import pickle
import os

from gamelearning.transformators import PaddleModel
from gamelearning.types import HandeledImage
from gamelearning.config import *


class TestPaddleModel(unittest.TestCase):
    def setUp(self):
        self.pm = PaddleModel()

        self.images = []
        self._load_test_images()

        self.handeled_image: HandeledImage = self.images[0]

    def test_handle(self):
        raw_result_was = self.handeled_image.raw_result
        text_was = self.handeled_image.text

        self.pm.handle([self.handeled_image])

        raw_result_became = self.handeled_image.raw_result
        text_became = self.handeled_image.text

        self.assertEqual(raw_result_was, raw_result_became)
        self.assertEqual(text_was, text_became)

    def _load_test_images(self):
        with open(str(PICKLE_OBJECTS_DIR) + os.path.sep + 'non_duplicate_images.pkl', 'rb') as imgs:
            self.images = pickle.load(imgs)



if __name__ == "__main__":
    unittest.main()
