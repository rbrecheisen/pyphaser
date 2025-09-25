import time
from pyphaser.pg.handigefuncties import Speler
from pyphaser.pg.handigefuncties import Vloer
from pyphaser.pg.handigefuncties import Ster
from pyphaser.pg.handigefuncties import Bom
from pyphaser.pg.handigefuncties import welke_keyboard_toetsen_zijn_ingedrukt
from pyphaser.pg.handigefuncties import wacht_een_paar_seconden


def main():

    speler = Speler()

    loopt_de_game_nog = 'JA'

    while loopt_de_game_nog == 'JA':

        keyboard_toetsen = welke_keyboard_toetsen_zijn_ingedrukt()
        
        if keyboard_toetsen['pijl_naar_links']:
            speler.beweeg_naar_links()

        elif keyboard_toetsen['pijl_naar_rechts']:
            speler.beweeg_naar_rechts()

        elif keyboard_toetsen['pijl_naar_boven'] or keyboard_toetsen['spatiebalk']:
            speler.spring()

        wacht_een_paar_seconden(1)


if __name__ == '__main__':
    main()