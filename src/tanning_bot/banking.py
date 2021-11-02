from walker import Walking
import pyautogui

class Banking(Walking):

    def __init__(self):
        Walking.__init__(self)
        self.all_button = False
        self.note_button = False

    def open_bank(self) -> None:
        """Opens the bank."""
        while self.find_closest_object(0) != []:
            coords = self.find_closest_object(0)
            # right click bank
            if coords != []:
                pyautogui.moveTo(coords, duration = 0.001)
                pyautogui.click(button = 'right')
                coords_button = self.locate_image_on_screen('images/bank_booth.png',0.7) 
                if coords_button != []:
                    # click open bank option
                    pyautogui.moveTo(coords_button[0][0], coords_button[0][1], duration = 0.1)
                    pyautogui.click()
                    while self.locate_image_on_screen('images/note_button_off.png', gray_scale = True) == []:
                        continue
                    break
                else:
                    continue   

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