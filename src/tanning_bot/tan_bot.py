from walker import Path, Area, Walking
from utilities import TakeBreak
from .hides_enum import Hide
from .banking import Banking
from .tanning import Tanning

class TanBot(Banking, Tanning, Walking, TakeBreak):
    
    bank_shop_path_walk = Path.ALKHARIDBANK_FRONT_TANSHOP_WALK.value
    bank_shop_path_run = Path.ALKHARIDBANK_FRONT_TANSHOP_RUN.value
    front_shop_area = Area.AL_KHARID_FRONT_TAN_SHOP.value
    tan_area = Area.AL_KHARID_TAN_SHOP.value
    shop_bank_path = Path.FRONT_TANSHOP_ALKHARIDBANK.value
    bank_area = Area.AL_KHARID_BANK.value

    def __init__(self):
        Walking.__init__(self)
        Banking.__init__(self)
        Tanning.__init__(self)
        TakeBreak.__init__(self)
        self.inv_open = False

    def walk_to_shop(self) -> None:
        """Walks to the tanning shop."""
        if not self.check_if_at_destination(self.tan_area):
            self.walk(self.bank_shop_path_walk, self.bank_shop_path_run, self.front_shop_area, self.tan_area, sleep_sec_run = 0.0, sleep_sec_walk = 3.2)
            while self.is_door_on_screen():
                self.open_door()

    def tan_hides(self, tanned_hide: Hide) -> None:
        """Tans the hides."""
        self.trade_ellis(tanned_hide)
        self.tan_hides_shop(tanned_hide)

    def walk_to_bank(self) -> None:
        """Walks to the bank."""
        if not self.check_if_at_destination(self.bank_area):
            while self.is_door_on_screen():
                self.open_door()
            self.walk(self.shop_bank_path, self.shop_bank_path, self.bank_area, sleep_sec_run = 0.5, sleep_sec_walk = 5.5)

    def handle_banking(self, hide: Hide, tanned_hide: Hide) -> None:
        """Deposits the tanned hides and withdraws hides."""
        self.open_bank()
        self.deposit_or_withdraw_all(tanned_hide[0], 'deposit')
        if self.locate_image_on_screen(hide[1], 0.7) == []:
            self.close_bank()
            self.logout()
            exit()
        self.deposit_or_withdraw_all(hide[1], 'withdraw')
        self.close_bank()

    def should_tan(self, hide: Hide) -> bool:
        """Returns whether we should be tanning."""
        return self.locate_image_on_screen(hide[0], 0.95) != []

    def should_bank(self, hide: Hide, tanned_hide: Hide) -> bool:
        """Returns whether we should be banking."""
        tanned_hide_inv = self.locate_image_on_screen(tanned_hide[0], 0.95) != []
        no_hides_inv = self.locate_image_on_screen(hide[0], 0.95) == []
        return tanned_hide_inv or no_hides_inv

    def run(self, hide: Hide, tanned_hide: Hide) -> None:
        """The logic of the bot, does the banking and tanning."""
        if self.inv_open == False:
            self.open_inv('images/open_inv.png')
            self.inv_open = True

        if self.should_tan(hide):
            self.walk_to_shop()
            self.tan_hides(tanned_hide)

        if self.should_bank(hide, tanned_hide):
            self.walk_to_bank()
            self.handle_banking(hide, tanned_hide)

