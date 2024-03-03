from .input_error import input_error


@input_error
def change_contact(args, contacts):
    name, new_phone_number = args
    try:
        if name in contacts:
            contacts[name] = int(new_phone_number)
            return "Contact updated."
        else:
            return "Contact not found."
    except ValueError:
        return "Invalid phone number format."
