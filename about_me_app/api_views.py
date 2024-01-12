from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .models import Aboutme
from .validate_and_error import (InvalidAPIUsage, validation_data,
                                 validation_patch_data)


@app.route('/api/aboutme/<string:nickname>/', methods=['GET'])
def get_about(nickname):
    """Получить данные об авторе по никнейму."""
    about = Aboutme.query.filter_by(nickname=nickname).first()
    if not about:
        raise InvalidAPIUsage(
            'Указанный никнейм не найден', HTTPStatus.NOT_FOUND
        )
    return jsonify({'about': about.to_dict()}), HTTPStatus.OK


@app.route('/api/aboutme/<string:nickname>/', methods=['PATCH'])
def update_about(nickname):
    """Редактировать данные об авторе по никнейму."""
    data = request.get_json(silent=True)
    validation_patch_data(data)
    if data is None:
        raise InvalidAPIUsage(
            'Некорректный запрос на изменение', HTTPStatus.UNSUPPORTED_MEDIA_TYPE
        )
    about = Aboutme.query.filter_by(nickname=nickname).first()
    if about is None:
        raise InvalidAPIUsage(
            'Что-то пошло не так, вероятно, вы поменяли никнейм.', HTTPStatus.BAD_GATEWAY  
        )
    about.name = data.get('name', about.name)
    about.surname = data.get('surname', about.surname)
    about.nickname = data.get('nickname', about.nickname)
    about.age = data.get('age', about.age)
    about.about_author = data.get('about_author', about.about_author)
    db.session.commit()
    return jsonify({'about': about.to_dict()}), HTTPStatus.CREATED


@app.route('/api/aboutme/', methods=['POST'])
def create_about():
    """Создать данные об авторе."""
    data = request.get_json(silent=True)
    validation_data(data)
    about = Aboutme()
    about.from_dict(data)
    db.session.add(about)
    db.session.commit()
    return jsonify(about.to_dict()), HTTPStatus.CREATED


@app.route('/api/aboutme/<string:nickname>/', methods=['DELETE'])
def delete_about(nickname):
    """Удалить данные об авторе."""
    about = Aboutme.query.filter_by(nickname=nickname).first()
    if about is None:
        raise InvalidAPIUsage(
            'Такой записи не существует', HTTPStatus.NOT_FOUND
        )
    db.session.delete(about)
    db.session.commit()
    return '', HTTPStatus.NO_CONTENT
