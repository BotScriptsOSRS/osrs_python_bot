from window_capture import WindowCapture
import pyautogui

# ONLY USED TO CONFIGURE OFFSETS, NOT TO RUN SCRIPT.

# Configuration
client_top_border = 27
client_side_border = 40
offset_minimap_x = 2438
offset_minimap_y = 110
offset_run_x = 2359
offset_run_y = 158

window = WindowCapture()
box = window.get_window('Runelite')

# pyautogui.displayMousePosition()

pyautogui.moveTo(offset_minimap_x,offset_minimap_y,2)
# # 2438 110
