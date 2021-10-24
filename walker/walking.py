import win32gui
import pyautogui

import math
import json

from time import sleep
from path_enum import Path


class Walking():

    degreesPerYaw: float = 360/2048

    def __init__(
        self,
        client_top_border: int,
        client_side_border: int,
        tiles_pixels: int,
        offset_minimap_x: float,
        offset_minimap_y: float,
        ):
        
        self.client_top_border = client_top_border
        self.client_side_border = client_side_border
        self.tiles_pixels = tiles_pixels
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

    def get_live_info(self, category: str) -> dict:
        '''Returns specific live information from the game client via the Status Socket plugin.'''
        try:
            f = open('live_data.json',)
            data = json.load(f)
            return data[category]
        except:
            pass

    def get_center_minimap(self, coordinates: list) -> list:
        '''Returns the coordinates of the center of the minimap.'''
        map_center_x = coordinates[0] + self.offset_minimap_x
        map_center_y = coordinates[1] - self.offset_minimap_y
        return [map_center_x, map_center_y]

    def compute_tiles(self, live_x: int, live_y: int, new_x: int, n_y: int) -> list:
        '''Returns the range to click from the minimap center in amount of tiles.'''      
        # Get live camera data.
        camera_data = self.get_live_info('camera')
        if camera_data != None:
            # Get camera angle.
            yaw = camera_data['yaw']
            # Account for anticlockwise OSRS minimap.
            degrees = 360 - self.degreesPerYaw*yaw
            # Turn degrees into pi-radians.
            theta = math.radians(degrees)
            # Turn position difference into pixels difference.
            x_reg = (new_x-live_x)*self.tiles_pixels
            y_reg = (live_y-n_y)*self.tiles_pixels
            # Formulas to compute norm of a vector in a rotated coordinate system.
            tiles_x = x_reg*math.cos(theta) +y_reg*math.sin(theta)
            tiles_y = -x_reg*math.sin(theta)+y_reg*math.cos(theta)
            return [round(tiles_x, 1), round(tiles_y, 1)]
        return [live_x, live_y]

    def change_position(self, center_mini: list, live_pos: list, new_pos: list):
        '''Clicks the minimap to change position'''
        tiles = self.compute_tiles(live_pos[0], live_pos[1], new_pos[0], new_pos[1])
        pyautogui.click(center_mini[0]+tiles[0], center_mini[1]+tiles[1])
        self.walking_wait(new_pos[0], new_pos[1])

    def walking_wait(self, new_x: int, new_y: int):
        '''Wait until finished walking.'''
        position_data = self.get_live_info('worldPoint')
        live_x, live_y = position_data['x'], position_data['y'] 
        while live_x != new_x  or live_y != new_y:
            position_data = self.get_live_info('worldPoint')
            if position_data == None:
                live_x, live_y = live_x, live_y
            else:
                live_x, live_y = position_data['x'], position_data['y']
            continue
        
    def walk(self, path: Path):
        '''Walks a path by clicking on the minimap'''
        while path:
            # Update position data.
            position_data = self.get_live_info('worldPoint')
            live_pos = [position_data['x'], position_data['y']]
            print(f'current: ({live_pos[0]},{live_pos[1]})')
            new_pos = path[0]
            print(f'target: ({new_pos[0]},{new_pos[1]})')
            self.change_position(self.center_minimap, live_pos, new_pos)
            # Wait for the map to catch up with live position.
            sleep(2)
            # Remove first coordinate.
            path.pop(0)

# path = Path.DRAYNOR_GE.value

# client_top_border = 30
# client_side_border = 50
# tiles_pixels = 5
# offset_minimap_x = 377.0
# offset_minimap_y = 195.0

# walker = Walking(client_top_border,
#                 client_side_border,
#                 tiles_pixels, 
#                 offset_minimap_x, 
#                 offset_minimap_y)

# walker.walk(path)
