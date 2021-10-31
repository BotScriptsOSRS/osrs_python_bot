from utilities import ObjectDetection
import pyautogui
from time import sleep

class Banking(ObjectDetection):

    def __init__(self):
        ObjectDetection.__init__(self)
        self.all_button = False
        self.note_button = False

    def open_bank(self) -> None:
        """Opens the bank."""
        coords = self.locate_image_on_screen('images/note_button_off.png')
        while coords == []:
            self.click_closest_object(0)
            sleep(2)
            coords = self.locate_image_on_screen('images/note_button_off.png')
        
    @staticmethod
    def close_bank() -> None:
        """Closes the bank."""
        pyautogui.press('esc')

    def deposit_or_withdraw_all(self, image_path: str, action: str) -> None:
        """Deposits or withdraws all items based on image path."""
        if action == 'withdraw':
            confidence = 0.7
        elif action == 'deposit':
            confidence = 0.95
        coords = self.locate_image_on_screen(image_path, confidence)
        if coords != []:
            pyautogui.moveTo(coords[0],duration = 0.2)
            pyautogui.click()
            sleep(1)
        
    def turn_on_button(self, button: str) -> None:
        """Turns on buttons in the bank based on image path."""
        if button == 'all':
            img_path = 'images/all_button_bank_off.png'
        elif button == 'note':
            img_path = 'images/note_button_off.png'
        elif button == 'item':
            img_path = 'images/item_button_off.png'

        coords = self.locate_image_on_screen(img_path)
        if coords != []:
            pyautogui.moveTo(coords[0],duration = 0.2)
            pyautogui.click()
            if button == 'all':
                self.all_button = True
            elif button == 'note':
                            self.note_button = True