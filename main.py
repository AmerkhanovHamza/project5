import pandas as pd
from functions import clean_phone_numbers

# Чтение файла .xlsx с номерами телефонов
data = pd.read_excel('file.xlsx')

# Очистка номеров телефонов
cleaned_data = clean_phone_numbers(data)

# Сохранение результата в новый файл с расширением .xlsx
cleaned_data.to_excel('cleaned_file.xlsx', index=False)
