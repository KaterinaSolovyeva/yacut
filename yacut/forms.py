import re

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, ValidationError
from wtforms.validators import DataRequired, Optional
from .models import URL_map


PATTERN = r'[a-zA-Z0-9]'


def is_correct(short_id):
    accord = re.findall(PATTERN, short_id)
    return ''.join(accord) == short_id


class URL_mapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки', validators=[Optional()]
    )
    submit = SubmitField('Создать')

    def validate_custom_id(form, field):
        if not is_correct(field.data):
            raise ValidationError('Указано недопустимое имя для короткой ссылки')
        if URL_map.query.filter_by(short=field.data).first():
            raise ValidationError(f'Имя {field.data} уже занято!')
