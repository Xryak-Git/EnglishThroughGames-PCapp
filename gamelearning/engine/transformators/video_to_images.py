from numpy import ndarray
import cv2
import os

from gamelearning.config import LEGEND_OF_HEROES_VIDEO, VIDEO_OUTPUT


class VideoToImages:
    def __init__(self,
                 video_path: str,
                 output_dir: str,
                 firts_seconds_to_skip: int = 0,
                 last_seconds_to_skip: int = 0,
                 every_n_seconds: int = 1
                 ):

        assert os.path.exists(video_path), "Не найдено видео"
        assert os.path.isdir(output_dir), "Каталог сохранения кадров не найден"
        assert isinstance(firts_seconds_to_skip, int)
        assert isinstance(last_seconds_to_skip, int)
        assert isinstance(every_n_seconds, int)
        assert all(map(lambda x: x >= 0, [firts_seconds_to_skip, last_seconds_to_skip]))
        assert every_n_seconds >= 1

        self.video_path = video_path
        self._output_dir = output_dir

        self._firts_seconds_to_skip = firts_seconds_to_skip
        self._last_second_to_skip = last_seconds_to_skip
        self._every_n_seconds = every_n_seconds

        self._fps = None
        self._frames_count = None
        self._seconds = None

        self._capture = cv2.VideoCapture(video_path)
        self._calculate_params()

    def _calculate_params(self):
        self._fps = int(self._capture.get(cv2.CAP_PROP_FPS))
        self._frames_count = int(self._capture.get(cv2.CAP_PROP_FRAME_COUNT))
        self._seconds = int(self._frames_count // self._fps)

    def extract_frames(self):
        for second in range(self._firts_seconds_to_skip, 
                            self._seconds - self._last_second_to_skip,
                            self._every_n_seconds):
            
            current_frame = second * self._fps
            self._capture.set(cv2.CAP_PROP_POS_FRAMES, current_frame)

            success, frame = self._capture.read()
            if success:
                self._save(frame=frame, name_postfix=second)
                print(second)

    def get_every_n_seconds(self) -> int:
        return self._every_n_seconds

    def set_every_n_seconds(self, n: int):
        assert isinstance(n, int)
        assert n >= 1

        self._every_n_seconds = n

    def release_capture(self):
        self._capture.release()
        print("Capture released")

    def _save(self, frame: ndarray, name_postfix: int):
        cv2.imwrite(rf'{self._output_dir}\frame_{name_postfix}.jpg', frame)


def main():
    video_handler = VideoToImages(
        video_path=str(LEGEND_OF_HEROES_VIDEO),
        output_dir=str(VIDEO_OUTPUT),
        firts_seconds_to_skip=1,
        every_n_seconds=3,
    )
    video_handler.extract_frames()


if __name__ == "__main__":
    main()
