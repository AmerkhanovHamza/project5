import pandas as pd

def clean_phone_numbers(data):
    # Очистка номеров телефонов от ненужных символов
    data['Телефон'] = data['Телефон'].str.replace(r'\D+', '', regex=True)
    return data
