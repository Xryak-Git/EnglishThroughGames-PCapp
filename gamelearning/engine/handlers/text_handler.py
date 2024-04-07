from thefuzz import fuzz
from typing import List

from gamelearning.types import HandeledImage
from gamelearning.config import FUZZ_PARTICAL_RATIO


class Deduplicator:
    def __init__(self):
        self._previous_image = None
        self._current_image = None

    def deduplicate(self, images: List[HandeledImage]):

        i = 0
        while i < len(images):

            self._current_image = images[i]
            self._previous_image = images[i - 1]

            if self._is_fuzz_found_duplicate():
                images.pop(i - 1)
                continue

            i += 1

    def _simple_deduplicate(self) -> bool:
        if self._previous_image.text in self._current_image.text:
            return True

    def _is_fuzz_found_duplicate(self) -> bool:
        if fuzz.partial_ratio(self._previous_image.text, self._current_image.text) > FUZZ_PARTICAL_RATIO:
            return True
