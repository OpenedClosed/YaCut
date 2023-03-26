"""
Файл, содержащий вспомогательные функции.
"""
import random
import re
import string

from flask import flash, render_template

from . import db
from .constants import PATTERN
from .error_handler import InvalidAPIUsage
from .models import URLMap


def get_unique_short_id(length):
    """
    Получить уникальную часть
    короткого url.
    """
    letters_and_digits = string.ascii_letters + string.digits
    unique_url_part = ''.join(random.sample(letters_and_digits, length))
    return unique_url_part


def check_and_create(short_id, is_api=False, data={}, form=None):
    """
    Проверить данные и создать
    объект, если все успешно.
    """
    if not is_api:
        data['url'] = form.original_link.data
    if not short_id or short_id == '':
        while (short_id in [url_map.short for url_map in URLMap.query.all()]) or (not short_id):
            short_id = get_unique_short_id(6)
    if short_id:
        pattern = re.compile(PATTERN)
        if not pattern.match(short_id):
            if is_api:
                raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
            flash('Указано недопустимое имя для короткой ссылки')
            return render_template('index.html', form=form)

    if URLMap.query.filter_by(short=short_id).first():
        if is_api:
            raise InvalidAPIUsage(f'Имя "{short_id}" уже занято.')
        flash(f'Имя {short_id} уже занято!')
        return render_template('index.html', form=form)
    data['custom_id'] = short_id
    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return url_map
