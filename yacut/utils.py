from random import choices
from string import ascii_letters, digits

from .constants import QUANTITY_CHAR
from .models import URLMap


def get_unique_short_id() -> str:
    """ Генерация ссылки. """
    while True:
        short_id = ''.join(choices(ascii_letters + digits, k=QUANTITY_CHAR))
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id
