from window_capture import WindowCapture
import pyautogui

# Configuration
client_top_border = 0
client_side_border = 0
offset_minimap_x = 0
offset_minimap_y = 0

window = WindowCapture(client_top_border,
                        client_side_border,
                        offset_minimap_x, 
                        offset_minimap_y)

box = window.get_window('Runelite')
coords = window.get_center_minimap(box)
print(coords)
pyautogui.displayMousePosition()
# pyautogui.click(coords)
# 
