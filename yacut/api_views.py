from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URL_map
from .views import get_unique_short_id


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original(short_id):
    map = URL_map.query.filter_by(short=short_id).first()
    if map is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify(url=map.original), 200


@app.route('/api/id/', methods=['POST'])
def add_short_link():
    data = request.get_json()
    if 'url' not in data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'custom_id' not in data or data['custom_id'] == '':
        short = get_unique_short_id()
    else:
        short = data['custom_id']
    if len(short) > 16:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки') 
    if URL_map.query.filter_by(short=short).first() is not None:
        raise InvalidAPIUsage('Эта ссылка уже занята')
    map = URL_map()
    data['original'] = data['url']
    data['short'] = short
    map.from_dict(data)
    db.session.add(map)
    db.session.commit()
    return jsonify(short_link='http://localhost/'+map.short, url=map.original), 201
