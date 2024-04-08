import numpy as np
import pprint

import os
import sys

__dir__ = os.path.dirname(__file__)
sys.path.append(os.path.join(__dir__, ''))


class HandeledImage:
    def __init__(self, title: str, image_path: str, image: np.ndarray):
        assert isinstance(title, str)
        assert isinstance(image_path, str)
        assert isinstance(image, np.ndarray)

        self._title = title
        self._image = image
        self._image_path = image_path

        self._text = None
        self._raw_result = None
        self._title_with_boxes = None
        self._image_with_boxes = None

    @property
    def title(self) -> str:
        return self._title

    @property
    def image(self) -> np.ndarray:
        return self._image

    @image.setter
    def image(self, image: np.ndarray):
        assert isinstance(image, np.ndarray)
        self._image = image

    @property
    def image_path(self) -> str:
        return self._image_path

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, text: str):
        assert isinstance(text, str)
        self._text = text

    @property
    def raw_result(self) -> list:
        return self._raw_result

    @raw_result.setter
    def raw_result(self, raw_result: list):
        assert isinstance(raw_result, list)
        self._raw_result = raw_result

    @property
    def boxes(self) -> np.ndarray:
        return self._image_with_boxes

    @boxes.setter
    def boxes(self, image_with_boxes: np.ndarray):
        assert isinstance(image_with_boxes, np.ndarray)

        self._image_with_boxes = image_with_boxes

    @property
    def title_boxes(self) -> str:
        return self._title_with_boxes

    @title_boxes.setter
    def title_boxes(self, title: str):
        assert isinstance(title, str)

        self._title_with_boxes = title

    def __str__(self) -> str:
        return pprint.pformat([self._title, self._image_path, self._text])
