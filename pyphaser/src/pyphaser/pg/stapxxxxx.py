from pyphaser.src.pyphaser.pg.handigefuncties import (
    welke_keyboard_toetsen_zijn_ingedrukt,
    wacht_een_paar_seconden,
)


def main():
    loopt_de_game_nog = 'ja'
    while loopt_de_game_nog == 'ja':
        keyboard_knoppen = welke_keyboard_toetsen_zijn_ingedrukt()
        print(keyboard_knoppen)
        wacht_een_paar_seconden(1)


if __name__ == '__main__':
    main()