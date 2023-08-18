"""YaCut Utilite
Copyright (C) 2023 Authors: Dmitry Korepanov, Yandex practikum
License Free
Version: 1.0.0.2023."""
from dotenv import load_dotenv
import os

load_dotenv()


class Config(object):
    """
    Настройки проекта YaCut.
    """

    SQLALCHEMY_DATABASE_URI: str = os.getenv(
        'DATABASE_URI',
        default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = os.getenv(
        'SQLALCHEMY_TRACK_MODIFICATIONS',
        default=None)
    SECRET_KEY: str = os.getenv(
        'SECRET_KEY',
        default='secret_code_must_be_here')
    FLASK_ENV: bool = os.getenv(
        'FLASK_ENV', default=False
    )
