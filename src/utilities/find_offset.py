from window_capture import WindowCapture
import pyautogui

# ONLY USED TO CONFIGURE OFFSETS, NOT TO RUN SCRIPT.

# Configuration
client_top_border = 28
client_side_border = 43
offset_minimap_x = 1359
offset_minimap_y = 83
offset_run_x = 78
offset_run_y = 49

window = WindowCapture()

box = window.get_window('Runelite')
coords = window.get_center_minimap(box)
print(coords)
#print("debug minimap center", coords)

pyautogui.displayMousePosition()
#pyautogui.moveTo(coords)
# 2360 160
