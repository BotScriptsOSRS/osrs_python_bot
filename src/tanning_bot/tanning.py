from walker import Walking
import pyautogui
import time

class Tanning(Walking):

    def __init__(self):
        Walking.__init__(self)

    def trade_ellis(self) -> None:
        """Trades the tanning NPC Ellis"""
        while self.find_closest_object(0) != []:
            coords = self.find_closest_object(0)
            # right click Ellis
            if coords != []:
                pyautogui.moveTo(coords, duration = 0.1)
                pyautogui.click(button = 'right')
                coords_trade = self.locate_image_on_screen('images/trade_ellis.png',0.7)
                if coords_trade != []:
                    # click trade option
                    pyautogui.moveTo(coords_trade[0][0], coords_trade[0][1], duration = 0.1)
                    pyautogui.click()
                    while self.locate_image_on_screen(self.tanned_hide[3], gray_scale = True) == []:
                        continue
                    break
                else:
                    continue            

    def tan_hides_shop(self) -> None:
        """Tans all hides in the inventory"""
        coords_tan_store = self.locate_image_on_screen(self.tanned_hide[3], 0.99 , True)
        if coords_tan_store != []:
            pyautogui.moveTo(coords_tan_store[0],duration = 0.2)
            pyautogui.click(button = 'right')
            # click all option
            self.click_image_on_screen('images/tan_all_button.png', 0.85)
            return
        coords_tan_hover = self.locate_image_on_screen('images/tan_hover.png',0.7, True)
        if coords_tan_store == [] and coords_tan_hover != []:
            pyautogui.click(button = 'right')
            # click all option
            self.click_image_on_screen('images/tan_all_button.png', 0.85)
        