from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


class URL_mapForm(FlaskForm):
    original = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле')]
    )
    short = StringField(
        'Ваш вариант короткой ссылки', 
        validators=[Length(1, 16), Optional()]
    )
    submit = SubmitField('Создать')
