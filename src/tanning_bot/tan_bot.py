from walker import Path, Area, Walking
from utilities import TakeBreak, Banking
from .hides_enum import Hide
from .tanning import Tanning
import pyautogui

class TanBot(Banking, Tanning, Walking, TakeBreak):
    
    bank_shop_path = Path.ALKHARIDBANK_FRONT_TANSHOP.value
    tan_area = Area.AL_KHARID_TAN_SHOP.value
    shop_bank_path = Path.FRONT_TANSHOP_ALKHARIDBANK.value
    bank_area = Area.AL_KHARID_BANK.value

    def __init__(self, hide: Hide, tanned_hide: Hide):
        Walking.__init__(self)
        Banking.__init__(self)
        Tanning.__init__(self)
        TakeBreak.__init__(self)
        self.inv_open = False
        self.hide = hide
        self.tanned_hide = tanned_hide
        self.get_task()
        
    def walk_to_shop(self) -> None:
        """Walks to the tanning shop."""
        if not self.check_if_at_destination(self.tan_area):
            self.walk(self.bank_shop_path, self.tan_area)
            while self.is_door_on_screen():
                self.open_door('images/open_door.png')

    def tan_hides(self) -> None:
        """Tans the hides."""
        self.trade_ellis()
        self.tan_hides_shop()
        self.should_tan = False
        self.should_bank = True

    def walk_to_bank(self) -> None:
        """Walks to the bank."""
        if not self.check_if_at_destination(self.bank_area):
            while self.is_door_on_screen():
                self.open_door('images/open_door.png')
            self.walk(self.shop_bank_path, self.bank_area)

    def handle_banking(self) -> None:
        """Deposits the tanned hides and withdraws hides."""
        self.open_bank()
        self.deposit_or_withdraw_all(self.tanned_hide[1], 'deposit')
        if self.locate_image_on_screen(self.hide[2], 0.7) == []:
            pyautogui.press('esc')
            self.logout()
            exit()
        self.deposit_or_withdraw_all(self.hide[2], 'withdraw')
        self.should_bank = False
        self.should_tan = True

    def get_task(self) -> None:
        """Returns whether we should be banking or tanning."""
        self.update_inventory()
        for item in self.inventory:
            if item['id'] == self.hide[0]:
                self.should_tan = True
                break
            self.should_tan = False
            if item['id'] == self.tanned_hide[0] or len(self.inventory)<2:
                self.should_bank =  True
                break
            self.should_bank =  False

    def run(self) -> None:
        """The logic of the bot, does the banking and tanning."""
        if self.inv_open == False:
            self.open_inv('images/open_inv.png')
            self.inv_open = True

        if self.should_tan == True:
            self.walk_to_shop()
            self.tan_hides()

        if self.should_bank == True:
            self.walk_to_bank()
            self.handle_banking()

