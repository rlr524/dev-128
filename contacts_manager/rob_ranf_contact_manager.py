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


def view_contacts(contacts: dict):
    viewed_contact = input("Enter the name: ").capitalize()
    if viewed_contact in contacts:
        print(f"Viewing contact for {viewed_contact}:\n")
        print(f"address: {contacts[viewed_contact].get('address', 'none')}")
        print(f"company: {contacts[viewed_contact].get('company', 'none')}")
        print(f"landline: {contacts[viewed_contact].get('landline', 'none')}")
        print(f"mobile: {contacts[viewed_contact].get('mobile', 'none')}")
        print(f"state: {contacts[viewed_contact].get('state', 'none')}")
    else:
        print("No contact found for that name.")


def add_contact(contacts: dict):
    name = input("Enter the name for the new contact: ").capitalize()

    if name in contacts:
        print(f"You already have a {name} in your contacts. Please enter "
              f"them by a nickname or another name\n")
    else:
        address = input("Enter the address for the new contact: ").title()
        company = input("Enter the company for the new contact (hit enter if "
                        "none): ").title()
        landline = input("Enter the landline number for the new contact (hit enter if "
                         "none): ")
        mobile = input("Enter the mobile number for the new contact (hit enter if "
                       "none): ")

        if company == "":
            company = "none"
        if landline == "":
            landline = "none"
        if mobile == "":
            mobile = "none"

        contacts[name] = {
            "address": address,
            "company": company,
            "landline": landline,
            "mobile": mobile
        }

        print(f"Contact {name} has been added.")


def delete_contact(contacts: dict):
    contact = input("Enter the name: ").capitalize()
    if contact in contacts:
        contacts.pop(contact)
        print(f"Contact for {contact} has been deleted.\n")
    else:
        print("There is no contact by that name.\n")


def display_fields(contacts: dict):
    field = input("Please enter the field you want to view: ")
    fields = []
    for contact in contacts:
        field_check = contacts[contact].get(field)
        fields.append(field_check)

    if len(fields) == 0:
        print("No contact found with that field.")
    else:
        print(f"Printing {field} for all contacts")
        for contact in contacts.keys():
            print(f"{contact}: {contacts[contact].get(field)}")


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
            view_contacts(contacts)
        elif user_command == "add":
            add_contact(contacts)
        elif user_command == "del":
            delete_contact(contacts)
        elif user_command == "field":
            display_fields(contacts)
        elif user_command == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
else:
    main()
