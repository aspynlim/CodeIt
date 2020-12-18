import random

user_input = int(input('Please enter a number: '))

# Generate a random number
random_num = round(100 * random.random() / 5)
if random_num == 0:
    random_num += 1

# Loop until a user guesses a number correctly.
count_try = 1

# Game
while count_try <= 4:
    count_left = 4 - count_try

    if user_input == random_num:
        print(f'Congratulations! You guessed {random_num} correctly after trying {count_try} time(s)!')
        break
    elif user_input > random_num:
        print('Down !')
        print(f'*** {random_num}')
        print(f'You have {count_left} opportunities left. Guess a number between 1 and 20: ')
        count_try += 1
        if count_try > 4:
            print(f'Oops...! The answer was {random_num}.')
            break
        else:
            user_input = int(input('Please enter a number: '))
    else:
        print('Up !')
        print(f'*** {random_num}')
        print(f'You have {count_left} opportunities left. Guess a number between 1 and 20: ')
        count_try += 1
        if count_try > 4:
            print(f'Oops...! The answer was {random_num}.')
            break
        else:
            user_input = int(input('Please enter a number: '))