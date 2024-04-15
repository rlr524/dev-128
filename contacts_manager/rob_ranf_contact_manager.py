# Assignment: DEV108 Contacts Manager
# Class: DEV 128
# Date 4/15/2024
# Author: Rob Ranf
# Description: Program to help user manage contacts information.


def display_menu():
    print("COMMAND MENU")
    print("list  - Display all contacts")
    print("view  - View a contact")
    print("add   - Add a contact")
    print("del   - Delete a contact")
    print("field - View field for all contacts")
    print("exit  - Exit program")


def list_contacts(contacts: dict):
    contacts = list(contacts.keys())
    contacts.sort()
    for c in contacts:
        print(f"{contacts.index(c) + 1}. {c}")


def view_contacts():
    return "view"


def add_contact():
    return "add"


def delete_contact():
    return "delete"


def display_fields():
    return "fields"


def main():
    contacts = {
        "Joel":
            {"address": "1500 Anystreet, San Francisco, 94110", "company": "A startup",
             "mobile": "555-555-1111"},
        "Anne":
            {"address": "1000 Somestreet, Fresno, CA 93704",
             "state": "California",
             "landline": "125-555-2222", "company": "Some Great Company"},
        "Sally":
            {"state": "Illinois", "landline": "217-555-1222",
             "company": "Illinois Technologies",
             "mobile": "217-333-2353"},
        "Ben":
            {"address": "1400 Another Street, Fresno CA 93704",
             "state": "California", "mobile": "125-555-4444"}
    }

    print("Welcome to the contacts manager program")

    display_menu()
    while True:
        user_command = input("Please enter the command: ").lower()
        if user_command == "list":
            list_contacts(contacts)
        elif user_command == "view":
            view_contacts()
        elif user_command == "add":
            add_contact()
        elif user_command == "del":
            delete_contact()
        elif user_command == "field":
            display_fields()
        elif user_command == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
else:
    main()
