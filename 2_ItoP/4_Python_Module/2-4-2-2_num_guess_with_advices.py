import random

RANDOM_NUM = round(100 * random.random() / 5)
if RANDOM_NUM == 0:
    RANDOM_NUM += 1
TRIES = 4

user_input = -1
count_try = 0


while user_input != RANDOM_NUM and count_try < TRIES:
    user_input = int(input(f'You have {TRIES - count_try} opportunities left. Guess a number between 1 and 20: '))
    count_try += 1

    if RANDOM_NUM > user_input:
        print('Up !')
        print(f'*** {RANDOM_NUM}')
    elif RANDOM_NUM < user_input:
        print('Down! ')
        print(f'*** {RANDOM_NUM}')

if user_input == RANDOM_NUM:
    print(f'Congratulations! You guessed {RANDOM_NUM} correctly after trying {count_try} time(s)!')
else:
    print(f'Oops...! The answer was {RANDOM_NUM}.')