import dearpygui.dearpygui as dpg

dpg.create_context()


def add_and_load_image(image_path, parent=None):
    width, height, channels, data = dpg.load_image(image_path)

    with dpg.texture_registry() as reg_id:
        texture_id = dpg.add_static_texture(width, height, data, parent=reg_id)

    if parent is None:
        return dpg.add_image(texture_id, width=300, height=300)
    else:
        return dpg.add_image(texture_id, parent=parent, width=300, height=300)


# _, _, _, data = dpg.load_image("Somefile.png")

path = r"C:\Users\igser\PycharmProjects\EnglishThrougGames\userdata\tmp"
images = ["frame_0_a6f2b84e-e6b3-44fb-b57d-8b81085c7702.jpg", "frame_1_2ff578e1-4c26-4824-afaa-2c4cbf713ea1.jpg",
          "frame_2_88f41e03-66aa-447d-8bc3-1665d7b36870.jpg"]
dataes = []

# for image in images:
#
#     _, _, _, data = dpg.load_image(fr"{path}\{image}")
#     dataes.append(data)
#     print(data)
#     print(fr"{path}\{image}")
#
# with dpg.texture_registry(show=True):
#     for i, data in enumerate(dataes):
#         dpg.add_static_texture(width=100, height=100, default_value=data, tag=f"texture_tag_{i}")

with dpg.window(label="Tutorial") as window:
    for i, image in enumerate(images):
        add_and_load_image(fr"{path}\{image}", window)

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
