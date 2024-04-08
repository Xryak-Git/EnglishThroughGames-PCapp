from typing import List, Tuple
from paddleocr import draw_ocr
from PIL import Image
import numpy as np
import os


from gamelearning.config import FONT_PATH
from gamelearning.engine.types import HandeledImage


class ImageAssignmentExeption(Exception):
    ...


class ImageHandler:
    def __init__(self):
        self._images: List[HandeledImage] = []

    # TODO: add check if with this crop_by impossible find text
    def crop_by(self, crop_params: Tuple[int, int, int, int]):
        assert self._images
        assert len(crop_params) == 4
        assert all(isinstance(item, int) for item in crop_params)

        for image in self._images:
            img = Image.fromarray(image.image)
            croped_img = img.crop(crop_params)

            image.image = np.array(croped_img)

    def draw_boxes(self):

        for image in self._images:
            if self._has_no_raw_result(image):
                continue

            self._draw_one_image_boxes(image)

    def save(self, path: str, draw_boxes=True):
        assert isinstance(path, str)
        assert isinstance(draw_boxes, bool)
        assert os.path.isdir(path)

        for image in self._images:
            self._common_save(path, image)
            self._save_with_boxes(path, image) if draw_boxes and image.boxes is not None else ...

    @staticmethod
    def _has_no_raw_result(image: HandeledImage) -> bool:
        return image.raw_result == [] or image.raw_result is None or image.raw_result == [None]

    def _save_with_boxes(self, path: str, image: HandeledImage):
        assert isinstance(image.boxes, np.ndarray)

        title_with_boxes = f"boxes_{image.title}"
        image.title_boxes = title_with_boxes

        pillow_image_with_boxes = Image.fromarray(image.boxes)
        pillow_image_with_boxes.save(fp=path + os.path.sep + title_with_boxes)

    def _common_save(self, path: str, image: HandeledImage):
        pillow_image = Image.fromarray(image.image)
        pillow_image.save(fp=path + os.path.sep + f"{image.title}")

    def _draw_one_image_boxes(self, image: HandeledImage):
        result = image.raw_result[0]
        img = Image.fromarray(image.image).convert('RGB')
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        im_show = draw_ocr(img, boxes, txts, scores, font_path=str(FONT_PATH))

        image.boxes = im_show

    @property
    def images(self) -> List[HandeledImage]:
        return self._images

    @images.setter
    def images(self, images: List[HandeledImage] | HandeledImage):
        if not (isinstance(images, list) or isinstance(images, HandeledImage)):
            raise ImageAssignmentExeption()

        if isinstance(images, list):
            assert all(isinstance(item, HandeledImage) for item in images)
            self._images = images

        elif isinstance(images, HandeledImage):
            self._images = [images]


def main():
    ...


if __name__ == "__main__":
    main()
