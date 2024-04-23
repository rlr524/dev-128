class Dog:
    name: str
    color: str
    is_hungry: bool
    weight: float

    def __init__(self, name: str, color: str, weight: float = 10):
        self.name = name
        self.color = color
        self.weight = weight
        self.is_hungry = True

    def bark(self):
        print(f"{self.name}: Woof Woof")

    def eat(self):
        self.is_hungry = False
        self.weight = self.weight + .1
        print(f"{self.name}: Chomp Chomp")

    def walk(self):
        if self.is_hungry:
            self.bark()
        else:
            self.weight = self.weight - .1
            self.is_hungry = True
            print(f"{self.name}: Step Step")

    def print_status(self):
        if self.is_hungry:
            print(f"{self.name} is {self.color}, weighs {self.weight}kg and is hungry.")
        else:
            print(f"{self.name} is {self.color}, weighs {self.weight}kg and is "
                  f"not hungry.")


def main():
    dog = Dog("Willie", "Brown", 15)
    print(f"{dog.name} welcomes you! Woof woof")

    while True:
        print("-" * 25)
        print("Enter a command")
        print(f"{'`S` to get Status inquiry,':{10}} {'`F` to feed the dog,'}")
        print(f"{'`W` to take it for a walk,':{10}} {'`Q` to exit:'}")
        command = input("").lower()
        if command == "s":
            dog.print_status()
        elif command == "w":
            dog.walk()
        elif command == "f":
            dog.eat()
        elif command == "q":
            print(f"Good bye! Woof woof")
            break
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
else:
    main()
