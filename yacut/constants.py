"""Для прохождения тестов не изменять строковые значения!"""

DESCRIPTION_CUST_URL: str = 'Ваш вариант короткой ссылки'
DESCRIPTION_ORIG_URL: str = 'Длинная ссылка'
ERROR_LEN: str = 'Длина ссылки не может быть больше 16 символов!'
ERROR_SHORT_URL: str = 'Указано недопустимое имя для короткой ссылки'
ERROR_URL: str = 'Некорректный URL!'
MISSING_DATA: str = 'Обязательное поле!'
# PATTERN_SHORT_URL - шаблон для генератора короткой ссылки
# ^ - начало строки; далее допустимы: большие латинские буквы,
# маленькие латинские буквы, цифры в диапазоне от 0 до 9 и
# _ нижнее подчеркивание; + сопоставляет предыдущий символ
# от одного до неограниченного количества раз, $ - конец строки,
# {1,16} - ограничение по количеству символов.
PATTERN_SHORT_URL: str = r'^[A-Za-z0-9_]{1,16}$'
# QUANTITY_CHAR - задает количество генерирууемых символов в utils.py
QUANTITY_CHAR: int = 6

ID_NOT_FREE: str = 'Имя "{}" уже занято.'
NOT_FOUND_SHORT_ID: str = 'Указанный id не найден'
MISSING_REQUEST_BODY: str = 'Отсутствует тело запроса'
URL_REQUIRED_FIELD: str = '"url" является обязательным полем!'
