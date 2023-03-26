"""
Файл, описывающий функции представления проекта.
"""
from flask import abort, redirect, render_template

from . import app
from .forms import LinksForm
from .models import URLMap
from .utils import check_and_create


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = LinksForm()
    if form.validate_on_submit():
        short_id = form.custom_id.data
        url_relation = check_and_create(short_id, is_api=False, data={}, form=form)
        if type(url_relation) is not str:
            return render_template(
                'index.html',
                short_url=url_relation.get_full_short_url(),
                form=form
            )
    return render_template('index.html', form=form)


@app.route('/<string:short>')
def redirector(short):
    url_map = URLMap.query.filter_by(short=short).first()
    if not url_map:
        abort(404)
    source_address = url_map.original
    return redirect(source_address, 302)
