# management
from contact_management.parse_input import parse_input
from contact_management.add_contact import add_contact
from contact_management.change_contact import change_contact
from contact_management.show_phone import show_phone
from contact_management.show_all import show_all


def main():
    contacts = {'Admin': '1234567890'}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "bye", "bb"]:
            print("Good bye!")
            break
        elif command in ["hello", "hi", "yo"]:
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
