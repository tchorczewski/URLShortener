from flask import Blueprint, request, render_template, abort, redirect
import validators
from worker.tasks import shorten_url
from app.instance.db_models import URLs

url_bp = Blueprint('shorten_url', __name__)


@url_bp.route('/', methods=['POST'])
def short_url():
    short_url_results = None
    if request.method == 'POST':
        url_data = request.form
        if validators.url(url_data['original_url']):
            short_url_results = shorten_url.delay(url_data, request.root_url).get() #Celery will not change task status on dev/test env - makes it impossible to actually obtain task results in a different way
        else:
            abort(400, description='Invalid URL provided')
    return render_template('index.html',  short_url=short_url_results)

@url_bp.route('/<string:code>', methods=['GET'])
def use_url(code):
    short_url_entry = URLs.query.filter_by(shortened_url=f'{request.url_root}{code}').first()
    if short_url_entry is None:
        return 'The shortened URL does not exist', 404
    original_url = short_url_entry.original_url
    if not original_url.startswith(('http://', 'https://')):
        original_url = 'https://' + original_url
    return redirect(original_url)
