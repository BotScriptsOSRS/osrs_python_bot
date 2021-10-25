from window_capture import WindowCapture
import pyautogui

# Configuration
client_top_border = 30
client_side_border = 50
offset_minimap_x = 102
offset_minimap_y = 110

window = WindowCapture(client_top_border,
                        client_side_border,
                        offset_minimap_x, 
                        offset_minimap_y)

box = window.get_window('Runelite')
coords = window.get_center_minimap(box)
print(coords)
# pyautogui.displayMousePosition()
pyautogui.click(coords)
# 2218 495