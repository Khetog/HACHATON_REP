import numpy as np
import pandas as pd

# Открываем файл Excel
file_name = "Test_file.xlsx"
df = pd.read_excel(file_name)

# Бесконечный цикл для поиска
while True:
    # Запрашиваем у пользователя поле для поиска
    search_field = input("Введите поле для поиска (например, 'Тип', 'Дата выхода', 'Название', 'Номер', 'Дата ввода действие', 'Ключевые слова') или 'exit' для выхода: ")

    # Проверяем, если пользователь ввел "exit", то выходим из цикла
    if search_field.lower() == 'exit':
        break

    # Запрашиваем у пользователя поисковой запрос
    search_query = input(f"Введите значение для поля '{search_field}' для поиска: ")

    # Выполняем поиск в соответствующем столбце
    if search_field in df.columns:
        result = df[df[search_field].astype(str).str.contains(search_query, case=False)]

        # Проверяем, были ли найдены совпадения
        if not result.empty:
            print("Результаты поиска:")
            print(result)
        else:
            print("Совпадений не найдено.")
    else:
        print(f"Поле '{search_field}' не существует в данных.")

# Закрываем программу
print("Программа завершена.")
