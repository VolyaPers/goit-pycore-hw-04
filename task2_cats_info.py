def get_cats_info(path):
    """
    Читає файл з інформацією про котів та повертає список словників.
    """
    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    cat_id, name, age = line.split(',')
                    cat_dict = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats_list.append(cat_dict)

        return cats_list

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено")
        return []


# Приклад використання
# Створюємо тестовий файл
test_file = "cats_file.txt"

with open(test_file, 'w', encoding='utf-8') as f:
    f.write("60b90c1c13067a15887e1ae1,Tayson,3\n")
    f.write("60b90c2413067a15887e1ae2,Vika,1\n")
    f.write("60b90c2e13067a15887e1ae3,Barsik,2\n")
    f.write("60b90c3b13067a15887e1ae4,Simon,12\n")
    f.write("60b90c4613067a15887e1ae5,Tessi,5\n")

cats_info = get_cats_info(test_file)
print(cats_info)
