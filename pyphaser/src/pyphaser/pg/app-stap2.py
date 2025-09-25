import time


def wacht_even(seconden):
    time.sleep(seconden)


def main():
    door_gaan = 'JA'
    while door_gaan == 'JA':
        print('Dit is de eerste stap!')
        wacht_even(1)


if __name__ == '__main__':
    main()