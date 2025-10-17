def total_salary(path: str) -> tuple[int, float]:
    """
    Аналізує файл із зарплатами розробників та обчислює статистику.
    """
    try:
        total = 0
        count = 0

        # Використовуємо контекстний менеджер для безпечної роботи з файлом
        with open(path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                # Видаляємо зайві пробіли та порожні рядки
                line = line.strip()
                if not line:
                    continue

                try:
                    # Розділяємо рядок на ім'я та зарплату
                    parts = line.split(',')

                    if len(parts) != 2:
                        raise ValueError(
                            f"Рядок {line_number}: невірний формат. "
                            f"Очікується 'Ім'я,зарплата', отримано: '{line}'"
                        )

                    name, salary_str = parts

                    # Перевіряємо, що ім'я не порожнє
                    if not name.strip():
                        raise ValueError(
                            f"Рядок {line_number}: ім'я розробника не може бути порожнім"
                        )

                    # Конвертуємо зарплату в число
                    try:
                        salary = int(salary_str.strip())
                        if salary < 0:
                            raise ValueError(
                                f"Рядок {line_number}: зарплата не може бути від'ємною"
                            )
                    except ValueError as e:
                        raise ValueError(
                            f"Рядок {line_number}: невірний формат зарплати '{salary_str}'. "
                            f"Очікується ціле число."
                        ) from e

                    total += salary
                    count += 1

                except ValueError as e:
                    # Передаємо помилку вище
                    raise e

        # Перевіряємо, чи файл містив хоча б один запис
        if count == 0:
            raise ValueError(
                f"Файл '{path}' порожній або не містить валідних даних про зарплати"
            )

        # Обчислюємо середню зарплату
        average = total / count

        return (total, average)

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Файл '{path}' не знайдено. Перевірте правильність шляху."
        )
    except UnicodeDecodeError as e:
        raise ValueError(
            f"Помилка читання файлу '{path}': невірне кодування. "
            f"Файл повинен бути у форматі UTF-8."
        ) from e


# Приклад використання
# Створимо тестовий файл для демонстрації
test_file = "salary_file.txt"

# Записуємо тестові дані
with open(test_file, 'w', encoding='utf-8') as f:
    f.write("Alex Korp,3000\n")
    f.write("Nikita Borisenko,2000\n")
    f.write("Sitarama Raju,1000\n")

try:
    total, average = total_salary(test_file)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except (FileNotFoundError, ValueError) as e:
    print(f"Помилка: {e}")
