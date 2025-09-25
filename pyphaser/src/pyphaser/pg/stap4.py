import time


def wacht_even(seconden):
    time.sleep(seconden)


def main():

    loopt_de_game_nog = 'JA'

    while loopt_de_game_nog == 'JA':
        wacht_even(1)


if __name__ == '__main__':
    main()