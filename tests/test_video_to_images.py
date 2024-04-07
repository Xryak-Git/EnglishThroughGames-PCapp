import unittest
import os

from gamelearning.engine.transformators import VideoToImages
from gamelearning.config import *


class TestVideoToImages(unittest.TestCase):

    def setUp(self):
        self._legend_of_heroes_video = str(LEGEND_OF_HEROES_VIDEO)
        self._persona3_video = str(PERSONA3_VIDEO)

    @staticmethod
    def _clear_output_dir(func):
        def inner(self):
            os.chdir(str(VIDEO_OUTPUT))
            for f in os.listdir(str(VIDEO_OUTPUT)):
                os.remove(f)
            print(f"Files in {VIDEO_OUTPUT} was deleted")

            func(self)

        return inner

    @_clear_output_dir
    def test_extract_frames_given_video_waiting_frames_same_as_second(self):
        vh = VideoToImages(
            video_path=self._legend_of_heroes_video,
            output_dir=str(VIDEO_OUTPUT),
        )
        vh.extract_frames()

        video_seconds = vh._seconds
        output_frames = len(os.listdir(str(VIDEO_OUTPUT)))

        self.assertEqual(video_seconds, output_frames)

    @_clear_output_dir
    def test_extract_frames_given_14_sec_video_with_skip_params_waiting_5_frames(self):
        vh = VideoToImages(
            video_path=self._legend_of_heroes_video,
            output_dir=str(VIDEO_OUTPUT),
            firts_seconds_to_skip=2,
            last_second_to_skip=2,
            every_n_seconds=2
        )
        vh.extract_frames()

        output_frames = len(os.listdir(str(VIDEO_OUTPUT)))

        self.assertEqual(5, output_frames)


if __name__ == "__main__":
    unittest.main()
