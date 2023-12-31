from typing import Any

from flask import (
    flash,
    redirect,
    render_template,
    request
)

from . import app, db
from .forms import URLForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view() -> str:
    """Создать оригинальную ссылку-идентификатор."""
    form = URLForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if not custom_id:
            custom_id = get_unique_short_id()
        elif URLMap.query.filter_by(short=custom_id).first():
            flash(f'Имя {custom_id} уже занято!')
            return render_template('yacut.html', form=form)
        url_map = URLMap(
            original=form.original_link.data,
            short=custom_id,
        )
        db.session.add(url_map)
        db.session.commit()
        flash(f'Новая ссылка готова: '
              f'<a href="{request.base_url}{custom_id}">'
              f'{request.base_url}{custom_id}</a>')
    return render_template('yacut.html', form=form)


@app.route('/<string:short_id>', methods=['GET'])
def yacut_view_redirect(short_id) -> Any:
    """Получить оригинальную ссылку по идентификатору."""
    return redirect(
        URLMap.query.filter_by(short=short_id).first_or_404().original)
