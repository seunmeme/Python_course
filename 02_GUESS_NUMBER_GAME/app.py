import random

print('---------------------------------')
print('    GUESS THAT NUMBER GAME')
print('---------------------------------')

number = random.randint(0,100)
guess = -1
name = input('Kindly enter a name: ')

while guess != number:
    user_input = input('Guess a number between 0 and 100: ')
    guess = int(user_input)

    if guess < number:
        print('Sorry {0}, Your guess of {1} is too low'.format(name, guess))
    elif guess > number:
        print('Sorry {}, Your guess of {} is too high'.format(name, guess))
    else:
        print('Excellent job {}, Your guess of {} is correct!'.format(name, guess))

print('Done.')
