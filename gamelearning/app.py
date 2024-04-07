from pathlib import Path
import sys, os

from gui import GUI
from engine import Engine
from gui.handlers import GUIHandler
from settings import DEFAULT_USER_DIR


def main():
    engine = Engine(DEFAULT_USER_DIR)
    handler = GUIHandler(engine)
    gui = GUI(handler)
    gui.run()


if __name__ == "__main__":
    main()
