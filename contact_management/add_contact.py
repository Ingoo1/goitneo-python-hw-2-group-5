from .input_error import input_error


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = int(phone)
    return f"Contact added. {name}: {phone}"
