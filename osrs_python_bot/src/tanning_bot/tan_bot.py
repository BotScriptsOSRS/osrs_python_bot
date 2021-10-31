from walker import Path, Area, Walking
from utilities import TakeBreak
from .hides_enum import Hide
from .banking import Banking
from .tanning import Tanning

class TanBot(Banking, Tanning, Walking, TakeBreak):
    
    bank_shop_path = Path.ALKHARIDBANK_FRONT_TANSHOP.value
    front_shop_area = Area.AL_KHARID_FRONT_TAN_SHOP.value
    front_inside_path = Path.FRONT_TAN_INSIDE.value
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
            self.walk(self.bank_shop_path, self.front_shop_area, 1)
            while self.is_door_on_screen():
                self.open_door()
            self.walk(self.front_inside_path, self.tan_area, 2)

    def tan_hides(self, tanned_hide: Hide) -> None:
        """Tans the hides."""
        self.trade_ellis(tanned_hide)
        self.tan_hides_shop(tanned_hide)

    def walk_to_bank(self) -> None:
        """Walks to the bank."""
        if not self.check_if_at_destination(self.bank_area):
            while self.is_door_on_screen():
                self.open_door()
            self.walk(self.shop_bank_path, self.bank_area,2)

    def handle_banking(self, hide: Hide, tanned_hide: Hide) -> None:
        """Deposits the tanned hides and withdraws hides."""
        self.open_bank()
        if self.all_button == False:
            self.turn_on_button('all')
        if self.note_button == False:
            self.turn_on_button('item')
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

