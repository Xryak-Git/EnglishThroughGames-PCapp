import unittest
import os
import re

from gamelearning.engine.handlers import ImageLoader
from gamelearning.config import *


class ImageLoaderWithOpenFields(ImageLoader):
    def __init__(self):
        super().__init__()

    @property
    def images_path(self):
        return self._images_path

    @property
    def images_names(self):
        return self._images_names


class TestImageLoader(unittest.TestCase):
    def setUp(self):
        self.loader = ImageLoaderWithOpenFields()

        self.images = None

    def test_load_not_existing_dir(self):
        with self.assertRaises(AssertionError):
            self.loader.load_images_path_and_name(path="dasjdasljk")

    def test_load_not_existing_image(self):
        with self.assertRaises(AssertionError):
            self.loader.load_one_image_path_and_name(path="dasjdasljk")

    def test_load_images_path_and_name_count(self):
        self.loader.load_images_path_and_name(str(IMAGES_INPUT))

        count = 0
        for filename in os.listdir(str(IMAGES_INPUT)):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                count += 1

        self.assertEqual(len(self.loader.images_path), count)
        self.assertEqual(len(self.loader.images_names), count)

    def test_load_images_in_alphabetic_order(self):
        self.loader.load_images_path_and_name(str(VIDEO_OUTPUT))

        self.assertEqual(self.loader.images_names, self._sorted_alphanumeric(self.loader.images_names))

    @staticmethod
    def _sorted_alphanumeric(data):
        convert = lambda text: int(text) if text.isdigit() else text.lower()
        alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
        return sorted(data, key=alphanum_key)

    def test_get_image_objects(self):
        ...


if __name__ == "__main__":
    unittest.main()
