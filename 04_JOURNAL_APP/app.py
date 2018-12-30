def main():
    print_header()
    run_event_loop()


def print_header():
    print('------------------------------')
    print('        JOURNAL APP        ')
    print('------------------------------')


def run_event_loop():
    print('What do you want to do with your journal?')

    cmd = None

    while cmd != 'x':
        cmd = input('[L]ist all entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries()
        elif cmd == 'a':
            add_entries()
        elif cmd != 'x':
            print("Sorry we don't understand '{}'.".format(cmd))


    print('Done. Goodbye!') 


def list_entries():
    print('Listing.......')


def add_entries():
    print('Adding.......')


main()