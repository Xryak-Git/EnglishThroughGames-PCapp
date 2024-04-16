import dearpygui.dearpygui as dpg
import os

from gamelearning.engine import Engine

from .uids import item_id
from gamelearning.settings import Settings, DEFAULT_PORCESSES


class GUIHandler:

    def __init__(self):
        ...

    def set_video_path(self, sender: str, app_data: dict):
        file_path = app_data["file_path_name"]
        dpg.set_value(item_id["labels"]["video_path"], file_path)

    def check_video_exists(self):
        ...

        # if os.path.exists(file_path):
        #     print("Файле найден")
        #     dpg.show_item(item_id["windows"]["video_params"])
        #     dpg.set_value(item_id["labels"]["video_path"], file_path)
        #     return
        # print("Файл не найден")

    def video_handle(self, video_params_root: int, *args, **kwargs):
        params = dpg.get_item_children(video_params_root, slot=1)

        if all(isinstance(param, int) for param in params):
            for param in params:
                value = dpg.get_value(param)
                print(value)

    def save_settings(self, sender, app_data, user_data: Settings):
        processes = dpg.get_value(item_id["labels"]["processes_number"])
        if self._processes_valid(processes):
            user_data.processes = processes
        else:
            user_data.processes = DEFAULT_PORCESSES

        user_data.write_to_file()

    def set_processes(self, sender: str, app_data: str):
        if self._processes_valid(app_data):
            return
        dpg.set_value(item_id["labels"]["processes_number"], "")

    def set_positive_integer(self, sender: str, value: str):
        if value.isnumeric() and int(value) >= 0:
            ...
        else:
            dpg.set_value(sender, "")

    def _extract_video_params(self):
        game_title = dpg.get_value(item_id["labels"]["game_title"])
        video_path = dpg.get_value(item_id["labels"]["video_path"])
        begining_skip = dpg.get_value(item_id["input_text"]["begining_skip"])
        end_skip = dpg.get_value(item_id["input_text"]["end_skip"])
        every_n_second = dpg.get_value(item_id["input_text"]["every_n_second"])
        video_params = {
            "game_title": game_title,
            "video_path": video_path,
            "begining_skip": begining_skip,
            "end_skip": end_skip,
            "every_n_second": every_n_second,
        }
        return video_params

    def _processes_valid(self, processes: str):
        if processes.isnumeric() and 1 <= int(processes) <= 8:
            return True
        return False

    def _validate_params(self, video_params):
        game_title = video_params["game_title"]

        if game_title != "" and all(param for param in video_params.values()):
            dpg.configure_item(item_id["input_text"]["video_params_error"], show=False)
            return True

        else:
            dpg.configure_item(item_id["input_text"]["video_params_error"], show=True)
            return False

    def _show_sucess_window(self):
        dpg.configure_item(item_id["windows"]["sucess_handle"], show=True)

    def _close_sucess_window(self):
        dpg.configure_item(item_id["windows"]["sucess_handle"], show=False)


    def _add_and_load_image(self, image_path, parent=None):
        width, height, channels, data = dpg.load_image(image_path)

        with dpg.texture_registry() as reg_id:
            texture_id = dpg.add_static_texture(width, height, data, parent=reg_id)

        if parent is None:
            return dpg.add_image(texture_id, width=300, height=300)
        else:
            return dpg.add_image(texture_id, parent=parent, width=300, height=300)


class GUItoEngine(GUIHandler):

    def __init__(self, engine: Engine):
        super().__init__()
        self._engine = engine

    def to_frames_press_button_processing(self, sender: str, value: str):
        video_params = self._extract_video_params()

        if self._validate_params(video_params):
            self._engine.video_to_frames(video_params)
            self._engine.load_images()

            self._show_sucess_window()

    def handle_images(self, sender, value):
        print("OK")
        self._close_sucess_window()

    def load_images_from(self, sender: str, value, user_data):
        path = ""
        files = []
        # if sender == item_id["buttons"]["load_images"]:
        path = self._engine.video_frames_path

        print(path)

        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            files.append(file_path)

        print(files)

        for image in files:
            self._add_and_load_image(image_path=image, parent=item_id["groups"]["static_images"])

        return files




