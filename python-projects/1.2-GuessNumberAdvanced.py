import random
import math

print('Hi welcome to the number guessing game.\nLet\'s start the game')

try:
    upper_range_user = input('Please, Enter the Upper range ... ')
    upper_range = int(upper_range_user)
except ValueError:
    raise Exception("Sorry, Upper Range isn'\t an integer")


try:
    lower_range_user = input('Please, Enter the lower range ... ')
    lower_range = int(lower_range_user)
except ValueError:
    raise Exception("Sorry, Lower Range isn'\t an integer")


guess_number = random.randrange(lower_range, upper_range)
attempt_no = math.floor(math.log2(upper_range - lower_range + 1))
guess_counter = 0

print(f'You have {attempt_no} attempts')

while guess_counter < attempt_no:

    guess_counter += 1
    my_guess = int(input('Please Enter your Guess : '))

    if my_guess == guess_number:
        print(f'The number is {guess_number} and you found it right !! in the {guess_counter} attempt')
        break

    elif guess_counter >= attempt_no and my_guess != guess_number:
        print(f'Oops sorry, The number is {guess_number} better luck next time')

    elif my_guess > guess_number:
        print('Your guess is higher')

    elif my_guess < guess_number:
        print('Your guess is lesser')

