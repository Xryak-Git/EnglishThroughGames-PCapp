import unittest
from gamelearning.engine.engine import Engine
from gamelearning.config import PROJECT_DIR
print(PROJECT_DIR)


class TestImageHandler(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = Engine(PROJECT_DIR)

    def test_video_to_frames(self):
        video_params = {
            "game_title": "PPek 1",
            "video_path": str(PROJECT_DIR / "Legend_of_heroes.mp4"),
            "begining_skip": 0,
            "end_skip": 0,
            "every_n_second": 1,
        }
        self.engine.video_to_frames(video_params)


if __name__ == "__main__":
    unittest.main()