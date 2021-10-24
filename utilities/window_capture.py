import win32gui

class WindowCapture():

    def __init__(
        self,
        client_top_border: int,
        client_side_border: int,
        offset_minimap_x: float,
        offset_minimap_y: float
        ):
        
        self.client_top_border = client_top_border
        self.client_side_border = client_side_border
        self.offset_minimap_x = offset_minimap_x
        self.offset_minimap_y = offset_minimap_y

        self.window = self.get_window('Runelite')
        self.center_window = self.find_center_window(self.window)
        self.center_minimap = self.get_center_minimap(self.center_window)

    def get_window(self, windowname: str) -> list:
        '''Returns the position of the window and the size of the window excluding the borders.'''
        # Get window handle.
        hwnd = win32gui.FindWindow(None, windowname)
        # Set window to foreground.
        win32gui.SetForegroundWindow(hwnd)
        # Get the window size.
        rect = win32gui.GetWindowRect(hwnd)
        # Adjust size for borders
        x = rect[0]
        y = rect[1] + self.client_top_border
        w = rect[2] - x - self.client_side_border
        h = rect[3] - y - self.client_top_border
        return [x, y, w, h]

    def find_center_window(self, window_features: list) -> list:
        '''Returns the center of the window, excluding the borders.'''
        x, y, w, h = window_features
        center_x = round(x+w/2)
        center_y = round(y+h/2)
        return [center_x, center_y]

    def get_center_minimap(self, coordinates: list) -> list:
        '''Returns the coordinates of the center of the minimap.'''
        map_center_x = coordinates[0] + self.offset_minimap_x
        map_center_y = coordinates[1] - self.offset_minimap_y
        return [map_center_x, map_center_y]
