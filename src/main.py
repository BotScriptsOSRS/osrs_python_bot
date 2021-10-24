from window_capture import WindowCapture
from walking import Walking
from data import Data
from path_enum import Path

# Configuration
client_top_border = 40
client_side_border = 60
tiles_pixels = 6
offset_minimap_x = 452.5
offset_minimap_y = 234.5

# Initiate classes
window = WindowCapture(client_top_border,
                        client_side_border,
                        offset_minimap_x, 
                        offset_minimap_y)
data = Data()
walker = Walking(window, data, tiles_pixels)

def main():
    path = Path.DRAYNOR_GE.value
    walker.walk(path)

if __name__ == '__main__':
    main()
