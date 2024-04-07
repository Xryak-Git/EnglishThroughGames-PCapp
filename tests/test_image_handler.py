from PIL import Image
import numpy as np
import unittest
import pickle
import os

from gamelearning.types import HandeledImage
from gamelearning.engine.handlers import ImageHandler
from gamelearning.config import *


class TestImageHandler(unittest.TestCase):
    def setUp(self) -> None:
        self.handler = ImageHandler()
        self.image_without_name_path = HandeledImage(
            image_path="",
            title="",
            image=np.array([])
        )

        self.output_dir = str(IMAGES_OUTPUT)

        self.images = []

        self._load_images()
        self._delete_files_in_dir(self.output_dir)

    def test_image_input_with_names_and_pathes(self):
        self.handler.images = self.images

    def test_image_input_one_without_name_and_pathe(self):
        self.images.append(self.image_without_name_path)

        self.handler.images = self.images

        self.images.pop(-1)

    def test_draw_boxes_without_raw_result(self):

        self.handler.images = self.image_without_name_path
        self.handler.draw_boxes()

    def test_draw_boxes_with_raw_result(self):
        hi = self.images[0]

        self.handler.images = hi
        self.handler.draw_boxes()

        hi = self.handler.images[0]

        self.assertIsNotNone(hi.boxes)

    def test_crop_right_format(self):
        crop_params = (0, 0, 1000, 1000)
        test_image = self.images[0]

        pillow_image = Image.fromarray(test_image.image)
        was_size = pillow_image.size

        self.handler.images = test_image
        self.handler.crop_by(crop_params)

        pillow_image = Image.fromarray(self.handler.images[0].image)
        became_size = pillow_image.size

        self.assertGreater(was_size, became_size)

    def test_crop_when_images_is_None(self):
        ih = ImageHandler()

        with self.assertRaises(AssertionError):
            ih.crop_by((0, 0, 1000, 1000))

    def test_save_images_count(self):
        files_was = self._get_files_count_in_dir(path=self.output_dir)

        self.handler.images = self.images
        self.handler.save(path=self.output_dir, draw_boxes=False)

        files_became = self._get_files_count_in_dir(path=self.output_dir)

        files_to_write = len(self.handler.images)

        self.assertEqual(files_became - files_was, files_to_write)

    def _load_images(self):
        with open(str(PICKLE_OBJECTS_DIR) + os.path.sep + 'non_duplicate_images.pkl', 'rb') as imgs:
            self.images = pickle.load(imgs)

    @staticmethod
    def _get_files_count_in_dir(path: str) -> int:
        return len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])

    @staticmethod
    def _delete_files_in_dir(path: str):
        os.chdir(path)
        all_files = os.listdir(path)

        for f in all_files:
            os.remove(f)


if __name__ == "__main__":
    unittest.main()
