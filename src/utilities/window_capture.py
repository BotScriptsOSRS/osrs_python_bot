
import win32gui
from typing import List
import time

class WindowCapture():

    CLIENT_TOP_BORDER: int = 27.0
    CLIENT_SIDE_BORDER: int = 40.0
    OFFSET_MINIMAP_X: float = -133.0
    OFFSET_MINIMAP_Y: float = 85.0
    OFFSET_RUN_X: float = 207.0
    OFFSET_RUN_Y: float = 166.0
    OFFSET_LOGOUT_X: float = 20.0
    OFFSET_LOGOUT_Y: float = 20.0

    def __init__(self):
        self.window = self.get_window('Runelite')
        self.center_screen = self.get_center_window(self.window)
        self.center_minimap = self.get_center_minimap(self.window)
        self.run_button = self.get_run_button(self.window)
        self.logout_cross = self.get_logout_cross(self.window)

    def get_window(self, windowname: str) -> List[int]:
        '''Returns the position of the window and the size of the window excluding the borders.'''
        # Get window handle.
        hwnd = win32gui.FindWindowEx(None, None, None, windowname)
        # Set window to foreground.
        time.sleep(3)
        win32gui.SetForegroundWindow(hwnd)
        print("Im a debug message after SetForegroundWindow")
        # Get the window size.
        rect = win32gui.GetWindowRect(hwnd)
        # Adjust size for borders
        x = rect[0]
        y = rect[1] + self.CLIENT_TOP_BORDER
        w = rect[2] - x - self.CLIENT_SIDE_BORDER
        h = rect[3] - y - self.CLIENT_TOP_BORDER
        print(x, y, w, h)
        return [x, y, w, h]

    def get_center_minimap(self, window_features: List[int]) -> List[float]:
        '''Returns the coordinates of the center of the minimap.'''
        map_center_x = window_features[0] + window_features[2] - self.OFFSET_MINIMAP_X
        map_center_y = window_features[1] + self.OFFSET_MINIMAP_Y
        return [map_center_x, map_center_y]

    def get_center_window(self, window_features: List[int]) -> List[int]:
        '''Returns the center of the window, excluding the borders.'''
        center_x = round(window_features[0]+window_features[2]/2)
        center_y = round(window_features[1]+window_features[3]/2)
        return [center_x, center_y]

    def get_run_button(self, window_features: List[int]) -> List[int]:
        run_x = window_features[0] + window_features[2] - self.OFFSET_RUN_X
        run_y = window_features[1] + self.OFFSET_RUN_Y
        return [run_x, run_y]

    def get_logout_cross(self,window_features: List[int]) -> List[int]:
        run_x = window_features[0] + window_features[2] - self.OFFSET_LOGOUT_X
        run_y = window_features[1] + self.OFFSET_LOGOUT_Y
        return [run_x, run_y]
