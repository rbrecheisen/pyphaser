import time


def wacht_even(seconden):
    time.sleep(seconden)


def main():
    doorgaan = 'JA'
    stap = 1
    while doorgaan == 'JA':
        print(f'Dit is stap: {stap}')
        stap = stap + 1
        wacht_even(1)


if __name__ == '__main__':
    main()