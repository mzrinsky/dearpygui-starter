#!/usr/bin/env python3

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

dpg.create_context()

default_font_size = 12
default_font_path = "/usr/share/fonts/TTF"
default_font_name = default_font_path + "/JuliaMono-Light.ttf"

with dpg.font_registry():
    default_font = dpg.add_font(default_font_name, default_font_size)
    # additional fonts cant be added here..
    # second_font = dpg.add_font("AdditionalFont.ttf", 20)

dpg.bind_font(default_font)

dpg.create_viewport(title="DearPyGui Starter Project")

def menu_callback(sender):
    print(f"Menu Item: {sender}")

# example viewport menu entry
with dpg.viewport_menu_bar():
    with dpg.menu(label="Menu"):
        dpg.add_menu_item(label="Menu Item #1", callback=menu_callback)
        dpg.add_menu_item(label="Menu Item #2", callback=menu_callback)
    with dpg.menu(label="Window"):
        dpg.add_menu_item(label="Debug", callback=lambda:dpg.show_tool(dpg.mvTool_Debug))
        dpg.add_menu_item(label="Style Editor", callback=lambda:dpg.show_tool(dpg.mvTool_Style))

# show the demo for now.. as there is nothing else interesting here atm.
demo.show_demo()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
