import random
import math

print('Hi welcome to the number guessing game.\nLet\'s start the game')
Upper_range_user = "Upper Range"
lower_range_user = "Lower Range"

def checkValue(value):
    try:
        x = input(f'Please, Enter the {value} ... ')
        value_convert = int(x)
        return value_convert
    except ValueError:
        raise Exception(f"Sorry, {value} isn'\t an integer")
    

upper_range = checkValue(Upper_range_user)
lower_range = checkValue(lower_range_user)

if lower_range >= upper_range:
    raise Exception(f"Sorry, Lower Range must be less than Upper Range")

guess_number = random.randrange(lower_range, upper_range)
attempt_no = math.floor(math.log2(upper_range - lower_range + 1))
guess_counter = 0

print(f'You have {attempt_no} attempts')

while guess_counter < attempt_no:

    guess_counter += 1
    my_guess = "Guess"
    my_guess = checkValue(my_guess)

    if my_guess == guess_number:
        print(f'The number is {guess_number} and you found it right !! in the {guess_counter} attempt')
        break

    elif guess_counter >= attempt_no and my_guess != guess_number:
        print(f'Oops sorry, The number is {guess_number} better luck next time')

    elif my_guess > guess_number:
        print('Your guess is higher')

    elif my_guess < guess_number:
        print('Your guess is lesser')

