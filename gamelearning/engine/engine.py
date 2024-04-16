from typing import List
import pickle
import os

from gamelearning.engine.types import HandeledImage
from gamelearning.config import *
from gamelearning.settings import Settings, SETTINGS_FILE

from .handlers import ImageHandler, ImageLoader, Deduplicator
from .transformators import VideoToImages, PaddleModel
from .database import *


class Engine:

    def __init__(self, base_dir: Path):
        self._base_dir = base_dir
        self._settings = Settings(self._base_dir / SETTINGS_FILE)
        self._db = db

        self._video_frames_path = self._settings.user_dir / "tmp"
        self._images_path = self._settings.user_dir / "images"
        self._images: list[HandeledImage] = []

        self._ih = ImageHandler()

        self._current_game = None

        self._make_user_dir()

    def video_to_frames(self, video_params: dict):
        self._delete_files_in(str(self._video_frames_path))

        video_handler = VideoToImages(video_path=video_params["video_path"],
                                      output_dir=str(self._video_frames_path),
                                      firts_seconds_to_skip=int(video_params["begining_skip"]),
                                      last_seconds_to_skip=int(video_params["end_skip"]),
                                      every_n_seconds=int(video_params["every_n_second"]))

        video_handler.extract_frames()
        video_handler.release_capture()

        self._add_game_title_if_not_extists(video_params)

    def load_images(self):
        il = ImageLoader()
        il.load_images_path_and_name(path=str(self._video_frames_path))
        self._images = il.get_image_objects()

    def extract_images_text(self):
        pm = PaddleModel()
        pm.handle(self._images)

    def deduplicate(self):
        dd = Deduplicator()
        dd.deduplicate(self._images)

    def save_images(self):
        self._ih.draw_boxes()
        self._ih.save(path=str(self._images_path), draw_boxes=True)

    def _add_game_title_if_not_extists(self, video_params):
        game_title = video_params["game_title"]
        game = Games.get_or_create(title=game_title)

        self._current_game = game

    @staticmethod
    def _delete_files_in(path: str):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)

    def _make_user_dir(self):
        Path(self._video_frames_path).mkdir(parents=True, exist_ok=True)
        Path(self._images_path).mkdir(parents=True, exist_ok=True)

    @property
    def video_frames_path(self):
        return self._video_frames_path


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
