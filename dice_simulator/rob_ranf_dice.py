# Assignment: DEV108 Review 2: Dice Simulator
# Class: DEV 128
# Date 4/7/2024
# Author: Rob Ranf
# Description: Program that simulates rolling of a 6-sided die and does some
# processing on the outcome.
import random


# The display_title() function prints the header.
def display_title():
    print("======================================")
    print("Welcome to the Dice Roller")
    print("")
    print("======================================")


# The roll() function simulates rolling a single 6-sided
# die and returns the result of the roll
def roll() -> int:
    result = random.randint(1, 6)
    return result


# The roll_dice() function accepts the count of rolls to be simulated as a positive
# integer input parameter. It then calls the roll function that many times, printing
# the resulting roll and adding it to a list. It returns the list to the caller.
def roll_dice(number_rolls: int) -> list[int]:
    rolls = []

    for _ in range(number_rolls):
        roll_result = roll()
        rolls.append(roll_result)

    return rolls


# The get_positive_count() function prompts the user for the count of rolls to be
# simulated. It validates that the number is greater than zero. If not, gives user
# feedback and prompts again. It uses exception handling to handle the case when user
# enters a non-integer input. It gives user appropriate feedback.
def get_positive_count():
    try:
        input_rolls = int(input("Enter the number of dice: "))
        while input_rolls < 1:
            print("Please enter a positive number.")
            input_rolls = int(input("Enter the number of dice: "))
    except ValueError:
        print("Please enter a whole number greater than zero.")


def main():
    display_title()
    get_positive_count()


if __name__ == "__main__":
    main()
else:
    main()
