def total_salary(path):
    # Открываем файл по указанному пути в режиме чтения с кодировкой UTF-8
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0  # Переменная для хранения общей суммы 
            count = 0  # Счетчик для количества записей
            for line in file:
                try:
                    # Разделяем строку, удаляем лишние пробелы
                    _, salary = line.strip().split(',')
                    total += int(salary.strip())  # Добавляем зарплату к общей сумме
                    count += 1
                except ValueError:
                    # Игнорируем строки с некорректным форматом
                    continue
            if count == 0:
                # Если записей нет, возвращаем 0 для суммы и среднего
                return 0, 0
            average = total / count  # Вычисляем среднюю зарплату
            return total, average  # Возвращаем общую сумму и среднюю зарплату
    except FileNotFoundError:
        # Обрабатываем, если файл не найден
        print(f"Ошибка: файл '{path}' не найден.")
        return 0, 0
    except Exception as e:
        # Обрабатываем другие исключения
        print(f"Произошла ошибка: {e}")
        return 0, 0

if __name__ == "__main__":
    # Указываем путь к файлу с данными о зарплатах
    path = "C:\Python_work\Work\PythonHW4\salary_file.txt" 
    total, average = total_salary(path)  # Вызываем функцию для подсчета зарплат
    # Выводим общую сумму и среднюю зарплату
    print(f"Общая сумма заработной платы: {total}, Средняя заработная плата: {average}")