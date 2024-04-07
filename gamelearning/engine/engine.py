from typing import List
import pickle
import time

from handlers import ImageHandler, ImageLoader, Deduplicator
from transformators import PaddleModel, VideoToImages
from gamelearning.types import HandeledImage
from gamelearning.config import *


def run():
    video_handler = VideoToImages(video_path=str(LEGEND_OF_HEROES_VIDEO), output_dir=str(VIDEO_OUTPUT), every_n_seconds=EVERY_N_SECOND)
    video_handler.extract_frames()
    video_handler.release_capture()

    crop_params = (450, 150, 1500, 300)

    il = ImageLoader()
    il.load_images_path_and_name(path=str(VIDEO_OUTPUT))
    images = il.get_image_objects()

    ih = ImageHandler()
    ih.images = images
    ih.crop_by(crop_params)

    pm = PaddleModel()
    pm.handle(ih.images)

    dd = Deduplicator()
    dd.deduplicate(images=ih.images)

    ih.draw_boxes()

    ih.save(path=str(IMAGES_OUTPUT), draw_boxes=True)


def pickle_save_images_objects(name: str, images: List[HandeledImage]):
    with open(f'{name}.pkl', 'wb') as outp:
        pickle.dump(images, outp, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    run()