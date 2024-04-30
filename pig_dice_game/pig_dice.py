from game import Game


def display_welcome():
    print("Let's play PIG!")
    print()
    print("* See how many turns it takes you to get to 20.")
    print("* Turn ends when you hold or roll a 1.")
    print("* If you roll a 1, you lose all points for the turn.")
    print("* If you hold, you save all points for the turn.")
    print()


def main():
    display_welcome()
    choice = "y"
    while choice.lower() == "y":
        game = Game()
        game.play()

        choice = input("Play again? (y/n): ")
        print()
    print("Bye!")


if __name__ == "__main__":
    main()
