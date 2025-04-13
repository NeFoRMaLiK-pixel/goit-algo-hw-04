def get_cats_info(path):
    try:
        cats = []  # Список для хранения информации о котах
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # Разделяем строку на ID, имя и возраст, удаляем лишние пробелы
                    cat_id, name, age = line.strip().split(',')
                    cat = {
                        "id": cat_id.strip(), 
                        "name": name.strip(),  
                        "age": age.strip()  
                    }
                    cats.append(cat)  # Добавляем информацию о коте в список
                except ValueError:
                    # Игнорируем строки с некорректным форматом
                    continue
        return cats  # Возвращаем список о котах
    except FileNotFoundError:
        # Обрабатываем случай, если файл не найден
        print(f"Ошибка: файл '{path}' не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []

if __name__ == "__main__":
    path = "C:/Python_work/Work/PythonHW4/cats_file.txt" 
    cats_info = get_cats_info(path)  # Вызываем функцию для получения информации о котах
    print("[\n" + ",\n".join([str(cat) for cat in cats_info]) + "\n]")