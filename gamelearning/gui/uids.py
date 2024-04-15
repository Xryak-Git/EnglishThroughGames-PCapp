import dearpygui.dearpygui as dpg

item_id = {
    "windows": {
        "main": dpg.generate_uuid(),
        "video_params": dpg.generate_uuid(),
        "settings": dpg.generate_uuid(),
        "sucess_handle": dpg.generate_uuid(),

    },
    "file_dialogs": {
        "video_select": dpg.generate_uuid(),
        "user_dir_select": dpg.generate_uuid(),

    },
    "labels": {
        "game_title": dpg.generate_uuid(),
        "video_path": dpg.generate_uuid(),
        "processes_number": dpg.generate_uuid(),

    },
    "buttons": {
        "save_settings": dpg.generate_uuid(),
        "to_frames_press_button_processing": dpg.generate_uuid(),
        "chose_video_path": dpg.generate_uuid(),
    },
    "input_text": {
        "begining_skip": dpg.generate_uuid(),
        "end_skip": dpg.generate_uuid(),
        "every_n_second": dpg.generate_uuid(),
        "video_params_error": dpg.generate_uuid(),

    },
}
