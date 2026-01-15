#python basic level

import random

#1 Generate a random number from input range and guess the number in 6 attempts
def first_challenge():
    #taking range input
    lower_range =int(input("Enter lower number range: "))
    upper_range =int(input("Enter upper number range: "))
    max_attempts = 6
    attempts = 0

    #selection of the random number to guess from input range
    number = random.randint(lower_range, upper_range)
    while attempts < max_attempts:
        attempts += 1
        input_number = int(input("Enter number: "))
        if input_number == number:
            print("You got it!")
            break
        elif input_number > number:
            print(f"Wrong! try smaller number, You have {max_attempts - attempts} attempts left")
        else:
            print(f"Wrong ! try bigger number, You have {max_attempts - attempts} attempts left")
    else:
        print("Sorry! you are out of attempts")

first_challenge()


