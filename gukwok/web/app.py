"""mod: 'gukwok.web.app'

"""

from flask import Flask, current_app, request, url_for, render_template
from flask import abort, make_response, jsonify, redirect

from gukwok import __version__
import gukwok.converter 


app = Flask(__name__, template_folder='templates')


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'message': 'bad request'}), 400)


@app.errorhandler(413)
def bad_request(error):
    return make_response(jsonify({'message': 'payload too large'}), 413)


@app.route('/')
def index():
    """gukwok index page"""
    return render_template('index.html')


@app.route('/result')
def result():
    return render_template('index.html')


@app.route('/api')
@app.route('/api/')
def to_api_index():
    return redirect(url_for('api_index'), code=301)


@app.route('/api/' + __version__)
@app.route('/api/' + __version__ + '/')
def api_index():
    return jsonify(
        {'message': 'index of api'})


@app.route('/api/' + __version__ 
    + '/<source>/<target>/', methods=["GET"])
def converter_null(source, target):
    abort(400)


@app.route('/api/' + __version__ 
    + '/<source>/<target>/<request>', methods=["GET"])
def converter(source, target, request):
    print(len(request))
    if not request:
        abort(400)
    if len(request) > 140:
        abort(413)
    return gukwok.converter.codec(source, target, request)