"""
Number guesser in Python. How the algorithm works:
1. User chooses a range
2. Program produces a random integer that the user must guess
3. If the user guesses too high then the program will print: Guess is too high!
4. If the user guesses too low then the program will print: Guess is too low!
5. Once the user guesses the number the program will print: You have guessed correctly!
6. Program terminates
"""

import random
import webbrowser

url = 'https://github.com/wickkan'

def gen_ran(int1: int, int2: int):
    assert type(int1) and type(int2) == int, "Arguments should be integers."
    lower = None
    upper = None
    guess = None
    if int1 == int2:
        lower = int1
        upper = int2
    elif int1 > int2:
        lower = int2
        upper = int1
    elif int1 < int2:
        lower = int1
        upper = int2
    random_int = random.randint(lower, upper)

    while guess != random_int:
        try:
            guess = int(input(("Guess a number between the range you provided: ")))
            if guess > random_int:
                print("Guess is too high!")
            elif guess < random_int:
                print("Guess is too low!")
            else:
                print("You have guessed correctly!")
        except ValueError:
            print("No whitespace or non-integers permitted!")


def gen_ran_ui():
    print('------------------ Number Guesser ------------------')
    int1 = None
    int2 = None
    while int1 is None:
        try:
            int1 = int(input("Enter range: "))
        except ValueError:
            print("No whitespace or non-integers permitted!")

    while int2 is None:
        try:
            int2 = int(input("Enter range: "))
        except ValueError:
            print("No whitespace or non-integers permitted!")
    gen_ran(int1, int2)
    print('*****------------------------------------------*****\n''Thanks for trying: Number Guesser\n''Click the link to check out more of my projects:\n', url)
    print('*****------------------------------------------*****')


if __name__ == '__main__':
    gen_ran_ui()
