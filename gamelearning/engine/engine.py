from typing import List
import pickle
import time
from pathlib import Path

from gamelearning.types import HandeledImage
from gamelearning.config import *
from gamelearning.settings import Settings, SETTINGS_FILE

from .handlers import ImageHandler, ImageLoader, Deduplicator
from .transformators import PaddleModel, VideoToImages


class Engine:
    _settings: Settings
    _base_dir: Path

    _video_frames_path: Path
    _images_path: Path
    _images: list[HandeledImage]

    _ih: ImageHandler

    def __init__(self, base_dir: Path):
        self._base_dir = base_dir
        self._settings = Settings(self._base_dir / SETTINGS_FILE)

        self._video_frames_path = self._settings.user_dir / "video_frames"
        self._images_path = self._settings.user_dir / "images"
        self._images = []

        self._ih = ImageHandler()

        self._make_user_dir()

    def video_to_frames(self, video_params: dict):
        video_handler = VideoToImages(video_path=video_params["video_path"],
                                      output_dir=str(self._video_frames_path),
                                      firts_seconds_to_skip=int(video_params["begining_skip"]),
                                      last_seconds_to_skip=int(video_params["end_skip"]),
                                      every_n_seconds=int(video_params["every_n_second"]))

        video_handler.extract_frames()
        video_handler.release_capture()


    def load_images(self):
        il = ImageLoader()
        il.load_images_path_and_name(path=str(self._video_frames_path))
        self._images = il.get_image_objects()

    def _make_user_dir(self):
        Path(self._video_frames_path).mkdir(parents=True, exist_ok=True)
        Path(self._images_path).mkdir(parents=True, exist_ok=True)




def run():
    ...
    # video_handler = VideoToImages(video_path=str(LEGEND_OF_HEROES_VIDEO), output_dir=str(VIDEO_OUTPUT),
    #                               every_n_seconds=EVERY_N_SECOND)
    # video_handler.extract_frames()
    # video_handler.release_capture()
    #
    # crop_params = (450, 150, 1500, 300)
    #
    # il = ImageLoader()
    # il.load_images_path_and_name(path=str(VIDEO_OUTPUT))
    # images = il.get_image_objects()
    #
    # ih = ImageHandler()
    # ih.images = images
    # ih.crop_by(crop_params)
    #
    # pm = PaddleModel()
    # pm.handle(ih.images)
    #
    # dd = Deduplicator()
    # dd.deduplicate(images=ih.images)
    #
    # ih.draw_boxes()
    #
    # ih.save(path=str(IMAGES_OUTPUT), draw_boxes=True)


def pickle_save_images_objects(name: str, images: List[HandeledImage]):
    with open(f'{name}.pkl', 'wb') as outp:
        pickle.dump(images, outp, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    run()
