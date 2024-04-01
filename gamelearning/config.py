from pathlib import Path

# Dirs
PROJECT_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = Path(__file__).resolve().parent

RESOURCES_DIR = PROJECT_DIR / "resources"
PICKLE_OBJECTS_DIR = RESOURCES_DIR / "pickle"

IMAGES_INPUT = RESOURCES_DIR / "input/images"
IMAGES_OUTPUT = RESOURCES_DIR / "output/images"

VIDEOS_INPUT = RESOURCES_DIR / "input/videos"
VIDEO_OUTPUT = RESOURCES_DIR / "output/videos"

# Static
FONT_PATH = BASE_DIR / "static/fonts/simfang.ttf"

# Video to images params
EVERY_N_SECOND = 1

# Text handler params
FUZZ_PARTICAL_RATIO = 80

# Multiprocessing
PROCESS_NUMBER = 2

# Test materails
TEST_IMG = RESOURCES_DIR / "input/images/3.jpg"
PERSONA3_VIDEO = RESOURCES_DIR / "input/videos/Persona3.mp4"
LEGEND_OF_HEROES_VIDEO = RESOURCES_DIR / "input/videos/Legend_of_heroes.mp4"


# Database
USER_ID = 1
