import random

print('---------------------------------')
print('    GUESS THAT NUMBER GAME')
print('---------------------------------')

number = random.randint(0,100)
guess = -1

while guess != number:
    user_input = input('Guess a number between 0 and 100: ')
    guess = int(user_input)

    if guess < number:
        print('Your guess is too low')
    elif guess > number:
        print('Your guess is too high')
    else:
        print('You win!')
        
print('Done.')
