"""
Файл, описывающий формы проекта.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


class LinksForm(FlaskForm):
    """
    Форма получения данных об url.
    """
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 256)]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки (необязательно)',
        validators=[Length(1, 16),
                    Optional()]
    )
    submit = SubmitField('Создать')
