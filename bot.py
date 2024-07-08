def parse_input(user_input):
    cmd, *args = user_input.strip().split()
    cmd = cmd.lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Невірний формат команди. Використовуйте: add [ім'я] [номер телефону]"
    name, phone = args
    contacts[name] = phone
    return "Контакт додано."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Невірний формат команди. Використовуйте: change [ім'я] [новий номер телефону]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Контакт оновлено."
    else:
        return "Контакт не знайдено."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Невірний формат команди. Використовуйте: phone [ім'я]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Контакт не знайдено."

def show_all(args, contacts):
    if args:
        return "Невірний формат команди. Використовуйте: all"
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "Контакти не знайдено."

def main():
    contacts = {}
    print("Вітаю! Я ваш помічник-бот.")
    print("Введіть одну з команд: ")
    print("hello - отримати привітання ")
    print("add [ім'я] [номер телефону] - додати новий контакт ")
    print("change [ім'я] [новий номер телефону] - змінити існуючий контакт ")
    print("phone [ім'я] - показати номер телефону для заданого контакту ")
    print("all - показати всі контакти")
    print("close або exit - завершити роботу бота")

    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("До побачення!")
            break
        elif command == "hello":
            print("Чим можу допомогти?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Невірна команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()