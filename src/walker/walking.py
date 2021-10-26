import pyautogui
import math

from time import sleep
from path_enum import Path
from data import Data
from window_capture import WindowCapture
from typing import List

class Walking():

    degreesPerYaw: float = 360/2048

    def __init__(self, window: WindowCapture, data: Data, tiles_pixels: int):
        self.center_minimap = window.center_minimap
        self.tiles_pixels = tiles_pixels
        self.data = data

    def compute_tiles(self, live_x: int, live_y: int, new_x: int, n_y: int) -> List[float]:
        '''Returns the range to click from the minimap center in amount of tiles.'''      
        # Get live camera data.
        camera_data = self.data.get_live_info('camera')
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

    def change_position(self, center_mini: List[float], live_pos: List[int], new_pos: List[int]) -> None:
        '''Clicks the minimap to change position'''
        tiles = self.compute_tiles(live_pos[0], live_pos[1], new_pos[0], new_pos[1])
        pyautogui.click(center_mini[0]+tiles[0], center_mini[1]+tiles[1])
        self.walking_wait(new_pos[0], new_pos[1])

    def walking_wait(self, new_x: int, new_y: int) -> None:
        '''Wait until finished walking.'''
        position_data = self.data.get_live_info('worldPoint')
        live_x, live_y = position_data['x'], position_data['y'] 
        while live_x != new_x  or live_y != new_y:
            position_data = self.data.get_live_info('worldPoint')
            if position_data == None:
                live_x, live_y = live_x, live_y
            else:
                live_x, live_y = position_data['x'], position_data['y']
            continue
        
    def walk(self, path: Path) -> None:
        '''Walks a path by clicking on the minimap'''
        while path:
            # Update position data.
            position_data = self.data.get_live_info('worldPoint')
            live_pos = [position_data['x'], position_data['y']]
            print(f'current: ({live_pos[0]},{live_pos[1]})')
            new_pos = path[0]
            print(f'target: ({new_pos[0]},{new_pos[1]})')
            self.change_position(self.center_minimap, live_pos, new_pos)
            # Wait for the map to catch up with live position.
            sleep(2)
            # Remove first coordinate.
            path.pop(0)


