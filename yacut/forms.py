from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Optional


class URL_mapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле')]
    )
    #Length(1, 16) убрано и условие перенесено во views для прохождения теста
    custom_id = StringField(
        'Ваш вариант короткой ссылки', validators=[Optional()]
    )
    submit = SubmitField('Создать')
