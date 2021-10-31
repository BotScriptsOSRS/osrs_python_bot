from .object_detection import ObjectDetection
import pyautogui
import random
from time import sleep

class TakeBreak(ObjectDetection):

    password = ''

    def __init__(self):
        ObjectDetection.__init__(self)

    def logout(self) -> None:
        """Logs out the player."""
        pyautogui.press('esc')
        pyautogui.moveTo(self.logout_cross, duration = 0.2)
        pyautogui.click()
        self.click_image_on_screen('images/click_here_to_logout.png')

    def login(self) -> None:
        """Logs in the player."""
        self.click_image_on_screen('images/existing_user_button.png')
        for i in self.password:
            pyautogui.press(i)
        self.click_image_on_screen('images/login_button.png')
        coords = self.locate_image_on_screen('images/click_here_to_play.png',0.7)
        while coords == []:
            coords = self.locate_image_on_screen('images/click_here_to_play.png',0.7)
        self.click_image_on_screen('images/click_here_to_play.png',0.7)
        sleep(2)
        
    def take_break(self) ->None:
        """Takes a break between 5 and 15 minutes."""
        self.logout()
        break_min = random.randint(5, 15)
        sleep(break_min*60)
        self.login()

