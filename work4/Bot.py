import re

def parse_input(user_input):
    # Разделяем ввод пользователя на команду и аргументы
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()  # Приводим команду к нижнему регистру
    return cmd, args

def add_contact(args, book):
    # Добавляем новый контакт или обновляем существующий
    name, phone = args
    if name not in book:
        book[name] = []  # Создаем запись, если контакта нет
    book[name].append(phone)  # Добавляем номер телефона
    return "Contact added/updated."

def change_contact(args, book):
    # Изменяем номер телефона существующего контакта
    name, phone = args
    if name in book:
        book[name] = [phone]  # Заменяем список телефонов новым номером
        return "Contact updated successfully"
    else:
        return "Contact not found"

def phone_contact(args, book):
    # Получаем номера телефонов по имени контакта
    name = args[0]
    if name in book:
        return ", ".join(book[name]) 
    else:
        return "Contact not found"

def show_all(book):
    # Показываем все контакты в адресной книге
    if not book:
        return "No contacts found" 
    return "\n".join([f"{name}: {', '.join(phones)}" for name, phones in book.items()])

def main():
    book = {} 
    print("Welcome to the assistant bot")
    while True:
        user_input = input("Please enter a command: ") 
        command, args = parse_input(user_input)  # Разбираем команду и аргументы
        if command in ["close", "exit"]:
            # Завершаем работу бота
            print("Good bye")
            break
        elif command == "hello":
            # Приветствие
            print("Hello! How can I help you today?")
        elif command == "add":
            # Добавление контакта
            print(add_contact(args, book))
        elif command == "change":
            # Изменение контакта
            print(change_contact(args, book))
        elif command == "phone":
            # Поиск телефона по имени
            print(phone_contact(args, book))
        elif command == "all":
            # Показ всех контактов
            print(show_all(book))
        else:
            # Обработка неизвестной команды
            print("Invalid command")
            
contacts_bot = main() 



