"""
Файл, описывающий модели проекта.
"""
from datetime import datetime

from flask import url_for

from yacut import db


class URLMap(db.Model):
    """
    Модель, связывающая исходный url
    с новым коротким url.
    """
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256))
    short = db.Column(db.String(128))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def get_full_short_url(self):
        """Получить короткую ссылку."""
        return url_for('index_view', _external=True) + self.short

    def to_dict(self):
        """Преобразовать данные к словарю."""
        return dict(
            url=self.original,
            short_link=self.get_full_short_url()
        )

    def from_dict(self, data):
        """
        Получить данные из словаря json и
        преобразовать их к нужному виду.
        """
        name_relation = {
            'url': 'original',
            'custom_id': 'short'
        }
        for key in name_relation:
            if key in data:
                setattr(self, name_relation[key], data[key])

        for key in name_relation:
            if key in data:
                setattr(self, name_relation[key], data[key])
