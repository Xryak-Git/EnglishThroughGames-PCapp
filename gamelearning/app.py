from pathlib import Path
import sys
import os

from gui import GUI
from engine import Engine
from gui.handlers import GUItoEngine
from settings import DEFAULT_USER_DIR
# from engine.database import *


def main():
    # db.connect()
    # db.create_tables([Users, Games, Videos,
    #                   LearningWords, Images, LearningWordsImages])
    # print(db.get_tables())

    engine = Engine(DEFAULT_USER_DIR)
    handler = GUItoEngine(engine)
    gui = GUI(handler)
    gui.run()


if __name__ == "__main__":
    main()
