from PIL import Image
import numpy as np
import os
import re

from gamelearning.engine.types import HandeledImage


class ImageLoader:
    def __init__(self):
        self._images_path = []
        self._images_names = []

    def load_images_path_and_name(self, path: str):
        assert isinstance(path, str)
        assert os.path.exists(path), "Каталог не найден"

        for filename in self._sorted_alphanumeric(os.listdir(path)):
            if self._has_valid_type(filename):
                img_path = str(path + os.path.sep + filename)

                self._images_path.append(img_path)
                self._images_names.append(filename)

    def load_one_image_path_and_name(self, path: str):
        assert isinstance(path, str)
        assert any(extension in path for extension in [".jpg", ".png"]), "Расширение должно быть .jpg или .png"
        assert os.path.isfile(path), "Изображение не получилось найти по этому пути"

        filename = os.path.basename(path).split('.')[0]

        self._images_path.append(path)
        self._images_names.append(filename)

    def get_image_objects(self) -> list[HandeledImage]:
        assert len(self._images_path) == len(self._images_names)

        images = []
        for i, path in enumerate(self._images_path):
            pill_image = Image.open(path)
            numpydata = np.asarray(pill_image)

            hi = HandeledImage(title=self._images_names[i], image_path=self._images_path[i], image=numpydata)
            images.append(hi)

        assert (all(isinstance(item, HandeledImage) for item in images))

        return images

    @staticmethod
    def _has_valid_type(filename: str) -> bool:
        return filename.endswith(".jpg") or filename.endswith(".png")

    @staticmethod
    def _sorted_alphanumeric(data: list[str]) -> list[str]:
        convert = lambda text: int(text) if text.isdigit() else text.lower()
        alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
        return sorted(data, key=alphanum_key)
