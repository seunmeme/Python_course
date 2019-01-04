import random
import time

from actors import Creature, Wizard


def main():
    print_header()
    game_loop()


def print_header():
    print('--------------------------------')
    print('        WIZARD BATTLE APP')
    print('--------------------------------')
    print()


def game_loop():
    creatures = [
        Creature('Toad', 1),
        Creature('Bat', 3),
        Creature('Tiger', 12),  
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)
    ]

    print(creatures)

    hero = Wizard('Gandalf', 75)

    while True:
        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest...'
        .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you want to [a]ttack, [r]unaway or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The wizard runs and hide, taking the time to recover...')
                time.sleep(7)
                print('The wizard returns revitalized!')
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!!!')
        elif cmd == 'l':
            print('The wizard {} takes a look at the surroundings and sees:'.format(hero.name))
            for c in creatures:
                print('* A {} of level {} '.format(
                    c.name, c.level
                ))
        else:
            print('Exiting game... Bye!')
            break

        print()


if __name__ == '__main__':
    main()
