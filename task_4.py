import sys


store = {}


def parse_input():
    data = input()
    cmd, *args = data.split()
    cmd = cmd.strip().lower()
    return cmd, args

def handle_command(parsed_message: list):
    match(parsed_message[0]):
        case "hello":
            print("How can I help you?")
        case "add":
            print(add_contact(parsed_message[1]))
        case "change":
            print(change_contact(parsed_message[1]))
        case "phone":
            print(show_phone(parsed_message[1][0]))
        case "all":
            print(show_all())
        case "exit":
            print("Good bye!")
            exit()
        case "close":
            print("Good bye!")
            exit()
        case _ :
            print("unknown command")

def add_contact(data: list):
    name, phone = data
    store[name] = phone
    return "Contact added."


def change_contact(data: list):
    name, phone = data
    if not store.get(name):
       return "Error: no such name."
    store[name] = phone
    return "Contact updated."

def show_phone(name):
    if not store.get(name):
        return "Error: no such name."
    return store[name]


def show_all():
    res = ""
    for name, phone in store.items():
        res += f"{name}: {phone}\n"
    return res


def exit():
    sys.exit(0)


def main():
    print("Welcome to the assistant bot!")
    while True:
        cmd = parse_input()
        handle_command(cmd)

main()