from abc import ABC, abstractmethod
from paddleocr import PaddleOCR
from typing import List, Tuple

from gamelearning.config import PROCESS_NUMBER
from gamelearning.types import HandeledImage

from multiprocessing import Pool


# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.


class ImageToText(ABC):
    @abstractmethod
    def handle(self, *args, **kwargs):
        raise NotImplementedError()


global global_ocr
global_ocr = PaddleOCR(use_angle_cls=True, lang='en')


class PaddleModel(ImageToText):

    @classmethod
    def handle(cls, images: List[HandeledImage]):
        assert isinstance(images, list)
        assert all(isinstance(item, HandeledImage) for item in images)

        with Pool(PROCESS_NUMBER) as p:
            images[:] = p.map(cls._handle, images)

        # 100 картинок с кропом только на диологи в Persona 3 видике
        # 1 -  145 секунд
        # 5 - 45 секунд
        # 10 - 36 секунд

    @classmethod
    def _handle(cls, image: HandeledImage) -> HandeledImage:
        raw_result, text = cls._try_get_text_and_raw_result(image)
        print(text)

        image.raw_result = raw_result
        image.text = "\n".join(text)
        return image

    @staticmethod
    def _try_get_text_and_raw_result(image: HandeledImage) -> Tuple[list, str]:
        raw_result, text = [], " "
        try:
            raw_result = global_ocr.ocr(img=image.image)
            text = [line[1][0] for line in raw_result[0]]
        except TypeError as ex:
            print(f"На кадре {image.title} не было найдено текста")
        return raw_result, text


def main():
    ...


if __name__ == "__main__":
    main()
