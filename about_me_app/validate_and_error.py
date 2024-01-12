from http import HTTPStatus
from re import search

from flask import jsonify

from . import app
from .models import Aboutme


class InvalidAPIUsage(Exception):
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    return jsonify(error.to_dict()), error.status_code


def validation_data(data):
    """Валидация данных."""
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if ('nickname' or 'about_author') not in data:
        raise InvalidAPIUsage('"nickname" и "about_author" являются обязательным полем!')
    if search(r"\s", data['nickname']):
        raise InvalidAPIUsage('Недопустимый никнейм, есть пробел!')
    if len(data['about_author']) < 1:
        raise InvalidAPIUsage('Пустое поле "о себе".')
    if Aboutme.query.filter_by(nickname=data['nickname']).first() is not None:
        raise InvalidAPIUsage(f'Никнейм "{data["nickname"]}" уже занят.')


def validation_patch_data(data):
    """Валидация данных при изменении."""
    if 'nickname' in data:
        if search(r"\s", data['nickname']):
            raise InvalidAPIUsage('Недопустимый никнейм, есть пробел!')
        if Aboutme.query.filter_by(nickname=data['nickname']).first() is not None:
            raise InvalidAPIUsage(f'Никнейм "{data["nickname"]}" уже занят.')
    if 'about_author' in data:
        if len(data['about_author']) < 1:
            raise InvalidAPIUsage('Пустое поле "о себе".')
