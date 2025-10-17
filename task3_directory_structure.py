import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізуємо colorama
init(autoreset=True)


def display_directory_structure(path, prefix=""):
    """
    Відображає структуру директорії з кольоровим виведенням.
    """
    try:
        directory = Path(path)

        # Перевіряємо, чи існує шлях
        if not directory.exists():
            print(f"{Fore.RED}Помилка: Шлях '{path}' не існує")
            return

        # Перевіряємо, чи це директорія
        if not directory.is_dir():
            print(f"{Fore.RED}Помилка: '{path}' не є директорією")
            return

        # Отримуємо список всіх елементів в директорії
        items = list(directory.iterdir())

        # Сортуємо: спочатку директорії, потім файли
        items.sort(key=lambda x: (not x.is_dir(), x.name))

        for index, item in enumerate(items):
            # Визначаємо, чи це останній елемент
            is_last = index == len(items) - 1

            # Вибираємо символи для виведення
            if is_last:
                connector = "┗"
                extension = "  "
            else:
                connector = "┣"
                extension = "┃ "

            if item.is_dir():
                # Директорія - синій колір
                print(f"{prefix}{connector} {Fore.BLUE}📂 {item.name}")
                # Рекурсивно виводимо вміст піддиректорії
                display_directory_structure(item, prefix + extension)
            else:
                # Файл - зелений колір
                print(f"{prefix}{connector} {Fore.GREEN}📜 {item.name}")

    except PermissionError:
        print(f"{Fore.RED}Помилка: Немає доступу до '{path}'")


def main():
    """
    Головна функція програми.
    """
    # Перевіряємо, чи передано аргумент
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: Потрібно вказати шлях до директорії")
        print(f"{Fore.YELLOW}Використання: python {sys.argv[0]} /шлях/до/директорії")
        return

    # Отримуємо шлях з аргументів командного рядка
    directory_path = sys.argv[1]

    # Виводимо заголовок
    print(f"\n{Fore.CYAN}Структура директорії: {Style.BRIGHT}{directory_path}\n")

    # Відображаємо структуру
    display_directory_structure(directory_path)

    print()  # Порожній рядок в кінці


if __name__ == "__main__":
    # Якщо аргументи не передано, показуємо приклад на тестовій директорії
    if len(sys.argv) < 2:
        # Визначаємо шлях до тестової директорії відносно скрипта
        script_dir = Path(__file__).parent
        test_dir = script_dir / "picture"

        print(f"{Fore.YELLOW}Приклад використання з тестовою директорією 'picture':\n")
        display_directory_structure(test_dir)
        print(f"\n{Fore.CYAN}Для використання з іншою директорією:")
        print(f"{Fore.YELLOW}python3 {sys.argv[0]} /шлях/до/директорії\n")
    else:
        main()
