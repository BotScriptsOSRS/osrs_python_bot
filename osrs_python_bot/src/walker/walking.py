import pyautogui
import math

from time import sleep
from .path_enum import Path
from .area_enum import Area
from utilities import Data, ObjectDetection
from typing import List


class Walking(Data, ObjectDetection):

    DEGREESPERYAW: float = 360/2048
    TILES_PIXELS = 5

    def __init__(self):
        Data.__init__(self)
        ObjectDetection.__init__(self)
        position_data = Data.get_live_info(self,'worldPoint')
        if position_data != None:
            self.live_pos = [position_data['x'], position_data['y']]

    def compute_tiles(self, live_x: int, live_y: int, new_x: int, n_y: int) -> List[float]:
        '''Returns the range to click from the minimap center in amount of tiles.'''      
        # Get live camera data.
        camera_data = self.get_live_info('camera')
        if camera_data != None:
            # Get camera angle.
            yaw = camera_data['yaw']
            # Account for anticlockwise OSRS minimap.
            degrees = 360 - self.DEGREESPERYAW*yaw
            # Turn degrees into pi-radians.
            theta = math.radians(degrees)
            # Turn position difference into pixels difference.
            x_reg = (new_x-live_x)*self.TILES_PIXELS
            y_reg = (live_y-n_y)*self.TILES_PIXELS
            # Formulas to compute norm of a vector in a rotated coordinate system.
            tiles_x = x_reg*math.cos(theta) +y_reg*math.sin(theta)
            tiles_y = -x_reg*math.sin(theta)+y_reg*math.cos(theta)
            return [round(tiles_x, 1), round(tiles_y, 1)]
        return []

    def change_position(self, center_mini: List[float], new_pos: List[int]) -> None:
        '''Clicks the minimap to change position'''
        tiles = self.compute_tiles(self.live_pos[0], self.live_pos[1], new_pos[0], new_pos[1])
        if tiles != []:
            pyautogui.moveTo(center_mini[0]+tiles[0], center_mini[1]+tiles[1])
            pyautogui.click()
            sleep(2)

    def get_target_pos(self, path: Path) -> List[int]:
        """Returns furthest possible coord."""
        idx = next(i for i in range(len(path)-1, -1, -1) if (abs(path[i][0]-self.live_pos[0]) <=13 and abs(path[i][1]-self.live_pos[1]) <=13))
        new_pos = path[idx]
        return new_pos

    def get_live_pos(self) -> List[int]:
        """Returns the current position of the player."""
        position_data = self.get_live_info('worldPoint')
        if position_data != None:
            self.live_pos = [position_data['x'], position_data['y']]

    def turn_run_on(self) -> None:
        """Turns on run if at 100% run energy."""
        coords = self.locate_image_on_screen('images/full_run.png', 0.95)
        if coords != []:
            x ,y = coords[0]
            pyautogui.moveTo(x,y, 0.2)
            pyautogui.click()

    def check_if_at_destination(self, area_destination: Area) -> bool:
        """Returns whether the player reached his destination."""
        bool_x = self.live_pos[0] in range(area_destination[0],area_destination[2]+1)
        bool_y = self.live_pos[1] in range(area_destination[1],area_destination[3]+1)
        return bool_x and bool_y

    def is_door_on_screen(self) -> bool:
        """Returns whether there is a closed marked door on the screen."""
        coords = self.find_closest_object(1)
        if coords == [0, 0]:
            return False
        else:
            return True

    def open_door(self) -> None:
        """Opens closed marked doors."""
        if self.is_door_on_screen():
            self.click_closest_object(1)
            sleep(1)

    def walk(self, path: Path, area_destination: Area, sleep_sec: int) -> None:
        '''Walks a path by clicking on the minimap'''
        while True:
            # If run is off and energy is at 100, turn on run.
            self.turn_run_on() # ~0.5 sec
            # Get live position.
            self.get_live_pos()
            new_pos = self.get_target_pos(path)
            # if not at destination and no door on screen, walk. Otherwise stop.
            if self.check_if_at_destination(area_destination):
                sleep(sleep_sec)
                break
            # Change position.
            self.change_position(self.center_minimap, new_pos)



