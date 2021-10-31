from window_capture import WindowCapture
import pyautogui

# ONLY USED TO CONFIGURE OFFSETS, NOT TO RUN SCRIPT.

# Configuration
client_top_border = 30
client_side_border = 50
offset_minimap_x = 103
offset_minimap_y = 110
offset_run_x = 207
offset_run_y = 166

window = WindowCapture()

box = window.get_window('Runelite')
x,y = window.run_button
print(window.run_button)
# pyautogui.displayMousePosition()
pyautogui.moveTo(x,y,2)
# 2174 487
