import numpy as np
import pandas as pd
'''file_name = "Test_file.xlsx"  # Замените на имя вашего Excel-файла

data = pd.read_excel(file_name)

# Выведите данные
print(data)'''
d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}
df = pd.DataFrame(d, index=["d", "b", "a"], columns=["two", "three"])
print('\n',df)