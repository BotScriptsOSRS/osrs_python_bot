import pyautogui
import math

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
        self.run_bool = False

    def compute_tiles(self, new_x: int, new_y: int) -> List[float]:
        '''Returns the range to click from the minimap center in amount of tiles.'''      
        # Get live camera data.
        self.update_camera_angle()
        # Account for anticlockwise OSRS minimap.
        degrees = 360 - self.DEGREESPERYAW*self.camera_angle
        # Turn degrees into pi-radians.
        theta = math.radians(degrees)
        # Turn position difference into pixels difference.
        self.update_positon()
        x_reg = (new_x-self.position[0])*self.TILES_PIXELS
        y_reg = (self.position[1]-new_y)*self.TILES_PIXELS
        # Formulas to compute norm of a vector in a rotated coordinate system.
        tiles_x = x_reg*math.cos(theta) +y_reg*math.sin(theta)
        tiles_y = -x_reg*math.sin(theta)+y_reg*math.cos(theta)
        return [round(tiles_x, 1), round(tiles_y, 1)]


    def change_position(self, new_pos: List[int]) -> None:
        '''Clicks the minimap to change position'''
        self.update_positon()
        tiles = self.compute_tiles(new_pos[0], new_pos[1])
        if tiles != []:
            pyautogui.moveTo(self.center_minimap[0]+tiles[0], self.center_minimap[1]+tiles[1], duration = 0.15)
            pyautogui.click()
            while abs(self.position[0] - new_pos[0]) > 5 or abs(self.position[1] - new_pos[1]) > 5:
                self.update_positon()
                continue

    def get_target_pos(self, path: Path) -> List[int]:
        """Returns furthest possible coord."""
        self.update_positon()
        idx = next(i for i in range(len(path)-1, -1, -1) if (abs(path[i][0]-self.position[0]) <=13 and abs(path[i][1]-self.position[1]) <=13))
        new_pos = path[idx]
        return new_pos

    def turn_run_on(self) -> None:
        """Turns on run energy."""
        pyautogui.moveTo(self.run_button, duration = 0.2)
        pyautogui.click()

    def check_if_at_destination(self, area_destination: Area) -> bool:
        """Returns whether the player reached his destination."""
        self.update_positon()
        bool_x = self.position[0] in range(area_destination[0],area_destination[2]+1)
        bool_y = self.position[1] in range(area_destination[1],area_destination[3]+1)
        return bool_x and bool_y

    def is_door_on_screen(self) -> bool:
        """Returns whether there is a closed marked door on the screen."""
        coords = self.find_closest_object(1)
        if coords == []:
            return False
        return True

    def open_door(self, img_path) -> None:
        """Opens closed marked doors."""
        while self.is_door_on_screen():
            coords = self.find_closest_object(1)
            pyautogui.moveTo(coords, duration = 0.2)
            if self.locate_image_on_screen(img_path, 0.7) != []:
                self.click_closest_object(1)
                while self.is_door_on_screen():
                    continue
                break

    def handle_running(self) -> None:
        """Turns on run if run energy is higher than 60."""
        # If run is off and run energy is larger than 60, turn on run.
        self.update_run_energy()
        if self.run_energy < 5 or self.run_energy == 100:
            self.run_bool = False
        if self.run_energy > 60 and self.run_bool == False:
            self.turn_run_on()
            self.run_bool = True

    def walk(self, path: Path, area_destination: Area) -> None:
        '''Walks a path by clicking on the minimap'''
        while True:
            # Turn on running if needed
            self.handle_running()
            # Get live position.
            new_pos = self.get_target_pos(path)
            # if not at destination and no door on screen, walk. Otherwise stop.
            if self.check_if_at_destination(area_destination):
                break
            # Change position.
            self.change_position(new_pos)
            if new_pos == path[-1]:
                while not self.check_if_at_destination(area_destination):
                    self.update_positon()
                    continue



