import dearpygui.dearpygui as dpg

from gamelearning.engine import Engine

from .uids import item_id
from .settings import Settings, DEFAULT_PORCESSES


class GUIHandler:

    def __init__(self, engine: Engine):
        self._engine = engine

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

    def to_frames(self, sender: str, value: str):
        video_path = dpg.get_value(item_id["labels"]["video_path"])
        begining_skip = dpg.get_value(item_id["input_text"]["begining_skip"])
        end_skip = dpg.get_value(item_id["input_text"]["end_skip"])
        every_n_second = dpg.get_value(item_id["input_text"]["every_n_second"])

        video_params = {
            "video_path": video_path,
            "begining_skip": begining_skip,
            "end_skip": end_skip,
            "every_n_second": every_n_second,
        }

        if all(param for param in video_params.values()):
            print(video_params)
            dpg.configure_item(item_id["input_text"]["video_params_error"], show=False)
        else:
            dpg.configure_item(item_id["input_text"]["video_params_error"], show=True)

    def _processes_valid(self, processes: str):
        if processes.isnumeric() and 1 <= int(processes) <= 8:
            return True
        return False
