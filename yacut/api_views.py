from flask import jsonify, request
from http import HTTPStatus

from . import app, db
from .error_handlers import InvalidAPIUsage
from .forms import is_correct
from .models import URL_map
from .views import get_unique_short_id


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original(short_id):
    map = URL_map.query.filter_by(short=short_id).first()
    if map is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify(url=map.original), 200


@app.route('/api/id/', methods=['POST'])
def add_short_link():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if 'custom_id' not in data or data['custom_id'] == '' or data['custom_id'] is None:
        short_id = get_unique_short_id()
    else:
        short_id = data['custom_id']
    if len(short_id) > 16:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки', HTTPStatus.BAD_REQUEST)
    if URL_map.query.filter_by(short=short_id).first() is not None:
        raise InvalidAPIUsage(f'Имя "{short_id}" уже занято.')
    if is_correct(short_id):
        map = URL_map()
        data['original'] = data['url']
        data['short'] = short_id
        map.from_dict(data)
        db.session.add(map)
        db.session.commit()
        return jsonify(short_link='http://localhost/' + map.short, url=map.original), HTTPStatus.CREATED
    else:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки', HTTPStatus.BAD_REQUEST)
