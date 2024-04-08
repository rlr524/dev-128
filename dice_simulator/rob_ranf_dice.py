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

    for i in range(number_rolls):
        roll_result = roll()
        rolls.append(roll_result)
        # Add one to the index to account for there is no roll number zero
        print(f"Die {i + 1}: {roll_result}")

    return rolls


# The get_positive_count() function prompts the user for the count of rolls to be
# simulated. It validates that the number is greater than zero. If not, gives user
# feedback and prompts again. It uses exception handling to handle the case when user
# enters a non-integer input. It gives user appropriate feedback.
def get_positive_count() -> int:
    while True:
        try:
            input_rolls = int(input("Enter the number of dice: "))
            while input_rolls < 1:
                print("Please enter a positive number.")
                input_rolls = int(input("Enter the number of dice: "))
            return input_rolls
        except ValueError:
            print("Please enter a whole number greater than zero.")


# The check_rolls_for_same() function checks all items in the list of rolls
# and returns True if all are the same, and False if they aren't all the same.
def check_rolls_for_same(rolls: list) -> bool:
    return all(i == rolls[0] for i in rolls)


# The check_rolls_for_value() function checks all items in the list of
# rolls for a specific value and returns True if the value is found.
def check_rolls_for_value(rolls: list, value: int) -> int:
    if rolls.count(value) > 0:
        return rolls.count(value)
    else:
        return 0


# The main() function is the program entry point.
def main():
    value_to_check = 6

    display_title()
    again = "y"
    while again == "y":
        rolls = get_positive_count()
        rolls_list = roll_dice(rolls)
        print("--------------------")
        print(f"Total: {sum(rolls_list)}")

        # Because the desired output is "All rolls..." plural, only run the function to
        # check if all rolls are the same if the player rolled more than one die.
        if len(rolls_list) > 1:
            same_rolls = check_rolls_for_same(rolls_list)
            if same_rolls:
                print("Yay! All rolls were the same!")

        has_value = check_rolls_for_value(rolls_list, value_to_check)
        if has_value > 0:
            print(f"Got {value_to_check} in {has_value} rolls.")
        else:
            print(f"Sorry! No {value_to_check} found!")

        again = input("Roll again? (y/n): ").lower()
    print("Goodbye!")


if __name__ == "__main__":
    main()
else:
    main()
