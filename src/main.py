from window_capture import WindowCapture
from walking import Walking
from data import Data
from path_enum import Path

# Configuration
client_top_border = 30
client_side_border = 50
tiles_pixels = 5
offset_minimap_x = 103.0
offset_minimap_y = 110.0

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
