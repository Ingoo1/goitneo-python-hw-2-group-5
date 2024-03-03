from .input_error import input_error


@input_error
def show_all(contacts):
    if len(contacts) >= 1:
        return "\n".join(
            [f"{name}: {phone_number}" for name, phone_number in contacts.items()]
        )
    else:
        return "No contacts found."
