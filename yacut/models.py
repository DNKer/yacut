from datetime import datetime
from typing import Any, Dict

from flask import url_for

from yacut import db


class URLMap(db.Model):
    """
    Модель "Ссылка":
    id - ключевое поле для ID
    original - поле для оригинальной длинной ссылки
    short - поле для короткого идентификатора
    timestamp - поле для временной метки; по этому столбцу БД будет проиндексирована
    """

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(64), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self) -> Dict[str, str]:
        """Серриализатор модели "Ссылка"."""
        return dict(
            url=self.original,
            short_link=url_for('yacut_view_redirect',
                               short_id=self.short,
                               _external=True))

    def from_dict(self, data) -> Any:
        """Десерриализатор модели "Ссылка"."""
        columns_dict = {'original': 'url', 'short': 'custom_id'}
        for field in columns_dict.items():
            if field[1] in data:
                setattr(self, field[0], data[field[1]])
