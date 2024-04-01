import unittest
import pickle
import os

from gamelearning.config import PICKLE_OBJECTS_DIR
from gamelearning.handlers import Deduplicator


class TestDeduplicator(unittest.TestCase):
    def setUp(self) -> None:
        self.deduplicator = Deduplicator()

        self.images = None

    def test_deduplicate_with_4_unic_images(self):
        self._load_duplicate_images()

        must_be = 4
        self.deduplicator.deduplicate(images=self.images)
        len_became = len(self.images)

        self.assertEqual(must_be, len_became)

    def test_deduplicate_without_duplicates(self):
        self._load_non_duplicate_images()

        len_was = len(self.images)
        self.deduplicator.deduplicate(images=self.images)
        len_became = len(self.images)

        self.assertEqual(len_was, len_became)

    def print_images(self):
        print("---" * 100)
        for image in self.images:
            print(image)
        print("---" * 100)

    def _load_duplicate_images(self):
        with open(str(PICKLE_OBJECTS_DIR) + os.path.sep + 'duplicate_images.pkl', 'rb') as imgs:
            self.images = pickle.load(imgs)

    def _load_non_duplicate_images(self):
        with open(str(PICKLE_OBJECTS_DIR) + os.path.sep + 'non_duplicate_images.pkl', 'rb') as imgs:
            self.images = pickle.load(imgs)


if __name__ == "__main__":
    unittest.main()
