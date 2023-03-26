"""
Файл, описывающий конфигурацию проекта.
"""
import os


class Config(object):
    """Класс настроек Flask проекта."""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
