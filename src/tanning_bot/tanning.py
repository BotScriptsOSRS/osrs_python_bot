from typing import List
from walker import Walking
import pyautogui

class Tanning(Walking):

    def __init__(self):
        Walking.__init__(self)

    def trade_ellis(self) -> List[int]:
        """Trades the tanning NPC Ellis"""
        while self.find_closest_object(0) != []:
            coords = self.find_closest_object(0)
            # right click Ellis
            if coords != []:
                pyautogui.moveTo(coords, duration = 0.1)
                pyautogui.click(button = 'right')
                coords_trade = self.locate_image_on_screen('images/trade_ellis.png',0.8)
                if coords_trade != []:
                    # click trade option
                    pyautogui.moveTo(coords_trade[0][0], coords_trade[0][1], duration = 0.1)
                    pyautogui.click()
                    coords_tan = self.locate_image_on_screen(self.tanned_hide[3], 0.99)
                    while coords_tan == [] or coords_tan[0] == None:
                        coords_tan = self.locate_image_on_screen(self.tanned_hide[3], 0.99)
                        continue
                    return coords_tan[0]
                else:
                    continue            

    def tan_hides_shop(self, coords_tan: List[int]) -> None:
        """Tans all hides in the inventory"""
        pyautogui.moveTo(coords_tan, duration = 0.15)
        pyautogui.click(button = 'right')
        # click all option
        pyautogui.moveTo(coords_tan[0]-20, coords_tan[1]+80, duration = 0.15)
        pyautogui.click()
          
