from utilities.window_capture import WindowCapture
from walker.walking import Walking
from utilities.data import Data
from path_enum import Path

# Configuration
client_top_border = 0
client_side_border = 0
tiles_pixels = 0
offset_minimap_x = 0.0
offset_minimap_y = 0.0

# Initiate classes
data = Data()
window = WindowCapture(client_top_border,
                        client_side_border,
                        offset_minimap_x, 
                        offset_minimap_y)
walker = Walking(window, data, tiles_pixels)

def main():
    path = Path.DRAYNOR_GE.value
    walker.walk(path)

if __name__ == '__main__':
    main()
