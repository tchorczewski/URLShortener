from __init__ import create_app
from flask import request, redirect, render_template, abort
from db import URLShortener
from tasks import shorten_url
import validators
from flask_swagger_ui import get_swaggerui_blueprint

app,celery = create_app()

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'

swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "URL Shortener API"
    }
)

app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def short_url():
    short_url_results = None
    if request.method == 'POST':
        url_data = request.form
        if validators.url(url_data['original_url']):
            short_url_results = shorten_url.delay(url_data, request.root_url).get() #Celery will not change task status on dev/test env - makes it impossible to actually obian task results in a different way
            print('Hej ', short_url_results)
        else :
            abort(400, description='Invalid URL provided')
    return render_template('index.html',  short_url=short_url_results)

@app.route('/<string:code>', methods=['GET'])
def use_url(code):
    short_url_entry = URLShortener.query.filter_by(shortened_url=f'{request.url_root}{code}').first()
    original_url = short_url_entry.original_url
    if not original_url.startswith(('http://', 'https://')):
        original_url = 'https://' + original_url
    return redirect(original_url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
