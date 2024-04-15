from gui import GUI
from engine import Engine
from gui.handlers import GUItoEngine
from settings import DEFAULT_USER_DIR


def main():
    engine = Engine(DEFAULT_USER_DIR)
    handler = GUItoEngine(engine)
    gui = GUI(handler)
    gui.run()


if __name__ == "__main__":
    main()
