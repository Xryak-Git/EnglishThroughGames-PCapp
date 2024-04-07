from gui import GUI
from engine import Engine
from gui.handlers import GUIHandler


def main():
    engine = Engine()
    handler = GUIHandler(engine)
    gui = GUI(handler)
    gui.run()


if __name__ == "__main__":
    main()
