"""
Файл, описывающий функции представления
к части API проекта.
"""
from http import HTTPStatus

from flask import jsonify, request

from . import app
from .error_handler import InvalidAPIUsage
from .models import URLMap
from .utils import check_and_create


@app.route('/api/id/', methods=['POST', ])
def get_short_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    required_field = 'url'
    if required_field not in data:
        raise InvalidAPIUsage(f'"{required_field}" является обязательным полем!')
    short_id = data.get('custom_id')
    url_map = check_and_create(short_id, is_api=True, data=data, form=None)
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET', ])
def get_original_url(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if not url_map:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    url = url_map.original
    return jsonify({'url': url}), HTTPStatus.OK
