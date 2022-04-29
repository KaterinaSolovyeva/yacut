from random import sample
from string import ascii_letters, digits

from flask import abort, flash, redirect, render_template

from . import app, db
from .forms import URL_mapForm
from .models import URL_map


def get_unique_short_id():
    letters_and_digits = ascii_letters + digits
    unique_short_id = ''.join(sample(letters_and_digits, 6))
    if URL_map.query.filter_by(short=unique_short_id).first():
        get_unique_short_id()
    return unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URL_mapForm()
    if form.validate_on_submit():
        short_name = form.custom_id.data
        if URL_map.query.filter_by(short=short_name).first():
            flash(f'Имя {short_name} уже занято!')
            form.custom_id.data = None
            return render_template('index.html', form=form)
        if short_name is None or short_name == '':
            form.custom_id.data = get_unique_short_id()
        if len(form.custom_id.data) > 16:
            flash('Указано недопустимое имя для короткой ссылки')
            form.custom_id.data = None
            return render_template('index.html', form=form)
        url_map = URL_map(
            original=form.original_link.data,
            short=form.custom_id.data,
        )
        db.session.add(url_map)
        db.session.commit()
    return render_template('index.html', form=form)


@app.route('/<string:short>')
def redirection_view(short):
    map = URL_map.query.filter_by(short=short).first()
    if map is not None:
        original_link = map.original
        return redirect(original_link)
    abort(404)
