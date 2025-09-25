import time
from pyphaser.pg.app import Player, Star, Bomb, Platform


def welke_keyboard_toetsen_zijn_ingedrukt():
    return [
        'Enter',
        'Pijl omhoog',
    ]


def wacht_een_paar_seconden(aantal_seconden):
    time.sleep(aantal_seconden)


class Speler(Player):
    def __init__(self):
        super(Speler, self).__init__()
        self.x = 0
        self.y = 0

    def beweeg_naar_links(self, stappen):
        pass

    def beweeg_naar_rechts(self, stappen):
        pass

    def spring(self, hoe_hoog):
        pass


class Ster(Star):
    pass


class Bom(Bomb):
    pass


class Vloer(Platform):
    pass