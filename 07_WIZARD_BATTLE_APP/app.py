def main():
    print_header()
    game_loop()


def print_header():
    print('--------------------------------')
    print('        WIZARD BATTLE APP')
    print('--------------------------------')
    print()


def game_loop():
    while True:
        cmd = input('Do you want to [a]ttack, [r]unaway or [l]ook around? ')
        if cmd == 'a':
            print('Attack')
        elif cmd == 'r':
            print('Running')
        elif cmd == 'l':
            print('Looking around')
        else:
            print('Exiting game... Bye!')
            break


if __name__ == '__main__':
    main()
