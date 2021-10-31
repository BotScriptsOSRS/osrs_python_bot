from tanning_bot.hides_enum import Hide
from utilities import ObjectDetection
import pyautogui
from time import sleep

class Tanning(ObjectDetection):

    def __init__(self):
        ObjectDetection.__init__(self)

    def trade_ellis(self, tanned_hide: Hide) -> None:
        """Trades the tanning NPC Ellis"""
        test_coords = self.locate_image_on_screen(tanned_hide[2])
        while test_coords == []:
            coords = self.find_closest_object(0)
            # right click Ellis
            if coords != []:
                pyautogui.moveTo(coords, duration = 0.1)
                pyautogui.click(button = 'right')
                # click trade option
                pyautogui.moveTo(coords[0],coords[1]+50, 0.1)
                pyautogui.click()
                sleep(2)
            test_coords = self.locate_image_on_screen(tanned_hide[2])

    def tan_hides_shop(self, tanned_hide: Hide) -> None:
        """Tans all hides in the inventory"""
        coords = self.locate_image_on_screen(tanned_hide[2], 0.99)
        if coords != []:
            pyautogui.moveTo(coords[0],duration = 0.2)
            pyautogui.click(button = 'right')
            # click all option
            pyautogui.moveTo(coords[0][0]-20, coords[0][1]+90)
            pyautogui.click()
