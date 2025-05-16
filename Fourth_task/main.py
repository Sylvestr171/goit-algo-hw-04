from random import choice
from pathlib import Path

#->->->->->->->->->->***FOURTH TASK***<-<-<-<-<-<-<-<-<-<

print ('\n\tFOURTH TASK\n')

#Функція розбору введеного користувачем рядку на команду та її аргументи. 
def parse_input(user_input:str) -> str:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

#Функція отриманн контакту Команда: "add John 1234567890"
def add_contact(args:str, contacts:dict):
    name, phone = args
    contacts[name.lower().capitalize()] = phone
    return "Contact added."

#Функція зміни контакту  Команда: "change John 0987654321"
def change_contact(args:str, contacts:dict) -> str:
    name, phone = args
    contacts[name.lower().capitalize()] = phone
    return 'Contact updated.'

#Функція показати контакти Команда: "phone John"
def show_phone(args:str, contacts:dict) -> str:
    name = args[0].lower().capitalize()
    return contacts.get(name, 'The name is missing')

#Функція виведення всієї адресної книги Команда: "all"
def show_all(contacts:dict):
   for key, value in contacts.items():
    print(f"{key} => {value}")


current_dir = Path(__file__).parent

#функція для вибору рандомної фрази для відповіді на hello
def get_random_phrase():
    try:
        with open(current_dir / "hello.txt", "r", encoding="utf-8") as file:
            phrase = file.readlines()
            return choice(phrase).strip()
    except FileNotFoundError:
        return "How can I help you?"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print(get_random_phrase())
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                show_all(contacts)
            case "help" | "?":
                print("""The bot helps to work with the contact book.
                        Commands and functions:
                        "close" | "exit" - exit the program
                        "hello" - display a greeting
                        "add <name> <phone_namer>" - add a phone number to the address book
                        "change <name> <phone_namer>" - change the phone number in the address book
                        "phone <name>" - show the number
                        "all" - show the entire address book
                        "help" | "?" - show this help""")             
            case _:
                print("Invalid command.\nFor help enter: ?, help")

if __name__ == "__main__":
    main()


#  Будь-яка команда, яка не відповідає вищезазначеним форматам, буде вважатися нами невірною, і бот буде виводити повідомлення "Invalid command."
     
