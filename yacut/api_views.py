from http import HTTPStatus as Status
from re import match
from typing import Any

from flask import jsonify, request

from . import app, db
from .constants import (
    ERROR_SHORT_URL,
    ID_NOT_FREE,
    MISSING_REQUEST_BODY,
    NOT_FOUND_SHORT_ID,
    PATTERN_SHORT_URL,
    URL_REQUIRED_FIELD
)
from .error_handlers import InvalidAPIUsageError
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def api_get_url(short_id) -> Any:
    """Получить объект по id и конвертировать данные в JSON."""
    url_redirect = URLMap.query.filter_by(short=short_id).first()
    if url_redirect is None:
        raise InvalidAPIUsageError(message=NOT_FOUND_SHORT_ID, status_code=Status.NOT_FOUND)
    return jsonify({'url': url_redirect.original}), Status.OK


@app.route('/api/id/', methods=['POST'])
def api_create_short_id() -> Any:
    """Создать объект и конвертировать данные в JSON."""
    data = request.get_json()
    if not data:
        raise InvalidAPIUsageError(message=MISSING_REQUEST_BODY, status_code=Status.BAD_REQUEST)
    if 'url' not in data:
        raise InvalidAPIUsageError(message=URL_REQUIRED_FIELD, status_code=Status.BAD_REQUEST)
    if data.get('custom_id') is None or not data.get('custom_id'):
        data['custom_id'] = get_unique_short_id()
    if URLMap.query.filter_by(short=data['custom_id']).first():
        raise InvalidAPIUsageError(ID_NOT_FREE.format(data['custom_id']))
    if not match(PATTERN_SHORT_URL, data['custom_id']):
        raise InvalidAPIUsageError(ERROR_SHORT_URL)
    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), Status.CREATED
