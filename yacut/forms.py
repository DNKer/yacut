from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import (
    DataRequired,
    Length,
    Optional,
    Regexp,
    URL,
)

from .constants import (
    ERROR_LEN,
    ERROR_SHORT_URL,
    ERROR_URL,
    DESCRIPTION_CUST_URL,
    DESCRIPTION_ORIG_URL,
    MISSING_DATA,
    PATTERN_SHORT_URL,
)


class URLForm(FlaskForm):
    """
    Форма с полями:
    original_link - обязательное для длинной исходной ссылки (models.original);
    custom_link - необязательное для пользовательского варианта короткой ссылки (models.short);
    submit - внести запись ("кнопка").
    """

    original_link = URLField(
        DESCRIPTION_ORIG_URL,
        validators=[DataRequired(message=MISSING_DATA),
                    URL(require_tld=True, message=ERROR_URL)]
    )
    custom_id = URLField(
        DESCRIPTION_CUST_URL,
        validators=[Length(1, 16, message=ERROR_LEN),
                    Optional(strip_whitespace=True),
                    Regexp(PATTERN_SHORT_URL, message=ERROR_SHORT_URL)]
    )
    submit = SubmitField('Создать')
