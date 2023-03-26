"""
Файл, описывающий конфигурацию проекта.
"""
import os


class Config(object):
    """Класс настроек Flask проекта."""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='any_secret_key')
