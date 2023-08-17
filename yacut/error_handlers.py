from http import HTTPStatus as Status
from typing import Any, Dict

from flask import jsonify, render_template

from . import app, db


class InvalidAPIUsageError(Exception):
    """
    Класс исключений. Конструктор класса принимает на вход текст
    сообщения и статус-код ошибки (необязательно). Если статус-код
    для ответа API не указан — вернется код 400.
    """
    status_code = Status.BAD_REQUEST

    def __init__(self, message, status_code=None) -> None:
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self) -> Dict[Any, Any]:
        """ Метод для сериализации переданного сообщения об ошибке. """
        return dict(message=self.message)


@app.errorhandler(InvalidAPIUsageError)
def invalid_api_usage(error) -> Any:
    """ Обработчик кастомного исключения для API. """
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(404)
def page_not_found(error) -> str:
    """ Обработка ошибки "Не найдено". """
    return render_template('404.html'), Status.NOT_FOUND


@app.errorhandler(500)
def internal_error(error) -> str:
    """ Обработка ошибки "Ошибка сервера". """
    db.session.rollback()
    return render_template('500.html'), Status.INTERNAL_SERVER_ERROR
