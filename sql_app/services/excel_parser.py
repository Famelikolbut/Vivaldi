import pandas as pd
import json


def parse_excel(file_data):
    try:
        # Загрузка данных из Excel файла в DataFrame с использованием pandas
        xls = pd.ExcelFile(file_data)
        sheet_names = xls.sheet_names  # Получение списка всех листов в файле

        parsed_data = {}

        # Парсинг данных для каждой страницы (листа) в файле
        for sheet_name in sheet_names:
            df = pd.read_excel(file_data, sheet_name=sheet_name)

            # Преобразование DataFrame в JSON для текущей страницы
            json_data = df.to_json(orient="records")

            # Парсинг JSON-строки и сохранение результатов в словарь
            parsed_data[sheet_name] = json.loads(json_data)

        return parsed_data
    except Exception as e:
        raise Exception(str(e))
