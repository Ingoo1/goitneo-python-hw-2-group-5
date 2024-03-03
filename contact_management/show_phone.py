from .input_error import input_error


@input_error
def show_phone(args, contacts):
    name = args[0]
    print(name)
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."
