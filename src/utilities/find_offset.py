from window_capture import WindowCapture
import pyautogui

# ONLY USED TO CONFIGURE OFFSETS, NOT TO RUN SCRIPT.

# Configuration
client_top_border = 27
client_side_border = 40
offset_minimap_x = -133
offset_minimap_y = 85
offset_run_x = -45
offset_run_y = 35

window = WindowCapture()

box = window.get_window('Runelite')
x,y = window.run_button
print(window.run_button)
print(type(window.run_button))
print(len(window.run_button))
pyautogui.displayMousePosition()
# pyautogui.moveTo(x,y,1)
# 2323 328
