import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="English through games")
dpg.configure_viewport(0, x_pos=300, y_pos=300, width=1000, height=800)

from .uids import item_id
from .handlers import GUIHandler
from gamelearning.settings import Settings, SETTINGS_FILE, DEFAULT_USER_DIR


settings_file = Settings(DEFAULT_USER_DIR / SETTINGS_FILE)
print(DEFAULT_USER_DIR)


class GUI:
    _h: GUIHandler

    def __init__(self, handler: GUIHandler):
        self._h = handler

    def run(self):
        self._make_gui()

        dpg.set_primary_window(item_id["windows"]["main"], True)

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()

    def _make_gui(self):
        with dpg.window(tag=item_id["windows"]["main"]):
            with dpg.menu_bar():
                with dpg.menu(label="File"):
                    self._make_settings()
                    self._make_video_params()

            dpg.add_button(tag=item_id["buttons"]["chose_video_path"], label="Chose video path",
                           callback=self._show_video_chose_dialog, show=True)

            dpg.add_input_text(tag=item_id["labels"]["video_path"], label="Video path",
                               readonly=True, width=500)

    def _make_settings(self):
        dpg.add_menu_item(label="Settings", callback=lambda: dpg.show_item(settings))

        with dpg.window(tag=item_id["windows"]["settings"],
                        show=False,
                        width=400) as settings:
            dpg.add_input_text(tag=item_id["labels"]["processes_number"], label="Process number",
                               hint="Must be integer 1 <= and >= 8", width=400, decimal=True,
                               default_value=str(settings_file.processes),
                               callback=self._h.set_processes)

            dpg.add_button(tag=item_id["buttons"]["save_settings"], label="Save",
                           callback=self._h.save_settings, user_data=settings_file)

    def _make_video_params(self):
        dpg.add_menu_item(label="Add video", callback=lambda: dpg.show_item(video_params))

        with dpg.window(tag=item_id["windows"]["video_params"],
                        show=False,
                        width=600, height=200) as video_params:
            dpg.add_button(tag=item_id["buttons"]["chose_video_path"], label="Chose video path",
                           callback=self._show_video_chose_dialog, show=True)

            dpg.add_input_text(tag=item_id["labels"]["video_path"], label="Video path",
                               readonly=True, width=500)

            with dpg.group():
                dpg.add_input_text(tag=item_id["input_text"]["begining_skip"],
                                   label="Skip seconds in the begining",
                                   default_value="0", width=200, decimal=True,
                                   hint="Must be positive integer",
                                   callback=self._h.set_positive_integer)

                dpg.add_input_text(tag=item_id["input_text"]["end_skip"],
                                   label="Skip seconds in the end",
                                   default_value="0", width=200, decimal=True,
                                   hint="Must be positive integer",
                                   callback=self._h.set_positive_integer)

                dpg.add_input_text(tag=item_id["input_text"]["every_n_second"],
                                   label="Take every n second",
                                   default_value="1", width=200, decimal=True,
                                   hint="Must be positive integer",
                                   callback=self._h.set_positive_integer)

            dpg.add_button(tag=item_id["buttons"]["to_frames"], label="To frames",
                           callback=self._h.to_frames)

            dpg.add_input_text(tag=item_id["input_text"]["video_params_error"],
                               default_value="Not all params are correct",
                               readonly=True,
                               show=False,
                               width=200)

    def _show_video_chose_dialog(self):

        if dpg.does_item_exist(item_id["file_dialogs"]["video_select"]):
            dpg.delete_item(item_id["file_dialogs"]["video_select"])

        with dpg.file_dialog(tag=item_id["file_dialogs"]["video_select"],
                             directory_selector=False,
                             show=True,
                             width=700, height=400,
                             callback=self._h.set_video_path):
            dpg.add_file_extension(".mp4", color=(150, 255, 150, 255), custom_text="[Video]")


if __name__ == "__main__":
    gui = GUI()
    gui.run()
