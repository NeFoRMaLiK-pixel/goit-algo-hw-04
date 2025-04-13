import sys
from pathlib import Path
from visualizer import Fore, Style, init  

init(autoresет=True)

def visualize_directory_structure(directory: Path, indent: str = ""):
    try:
        for item in directory.iterdir():
            if item.is_dir():
                # Выводим имя директории с синим цветом
                print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}/")
                # Рекурсивно обрабатываем вложенные директории
                visualize_directory_structure(item, indent + "    ")
            else:
                # Выводим имя файла с зеленым цветом
                print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
    except PermissionError:
        # Обрабатываем ошибку доступа к директории
        print(f"{indent}{Fore.RED}Доступ запрещен: {directory}{Style.RESET_ALL}")

def main():
    if len(sys.argv) != 2:
        # Проверяем, передан ли путь к директории в аргументах
        print(f"{Fore.RED}Ошибка: Укажите путь к директории в качестве аргумента.{Style.RESET_ALL}")
        sys.exit(1)

    directory_path = Path(sys.argv[1])  # Получаем путь к директории из аргументов

    if not directory_path.exists():
        # Проверяем путь
        print(f"{Fore.RED}Ошибка: Указанный путь не существует.{Style.RESET_ALL}")
        sys.exit(1)

    if not directory_path.is_dir():
        # Проверяем путь на директорию
        print(f"{Fore.RED}Ошибка: Указанный путь не является директорией.{Style.RESET_ALL}")
        sys.exit(1)

    # Выводим заголовок структуры директории
    print(f"{Fore.YELLOW}Структура директории: {directory_path}{Style.RESET_ALL}")
    visualize_directory_structure(directory_path) 

if __name__ == "__main__":
    main()  