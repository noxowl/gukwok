"""mod: 'gukwok.web.app'

"""

from packaging.version import Version, LegacyVersion
from flask import Flask, current_app, request, url_for, render_template,\
                    abort, make_response, jsonify, redirect, flash
from wtforms import Form, TextField, TextAreaField, validators,\
                    StringField, SubmitField

from gukwok import __version__, legacy_version
import gukwok 


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = ''

def is_legacy(version):
    return Version(version) < Version(legacy_version)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'message': 'bad request'}), 400)


@app.errorhandler(413)
def bad_request(error):
    return make_response(jsonify({'message': 'payload too large'}), 413)


@app.route('/', methods=['GET', 'POST'])
def index():
    """gukwok index page"""
    form = gukwok.converter.ConvertForm(request.form)

    print("error " + str(form.errors))
    if request.method == 'POST':
        source = request.form['source']
        print(source)

        if form.validate():
            flash(gukwok.converter.codec('euckr', 'sjis', source))
        else:
            flash('source required.')
    return render_template('index.html', form=form)


@app.route('/api')
@app.route('/api/')
def to_api_index():
    return redirect(url_for('api_index'), code=301)


@app.route('/api/<version>')
@app.route('/api/<version>/')
def api_index(version):
    if is_legacy(version):
        abort(416)
    return jsonify(
        {'message': 'index of api'})


@app.route('/api/<version>/source>/<target>/', methods=["GET"])
def converter_null(source, target):
    abort(400)


@app.route('/api/<version>/source>/<target>/<request>', methods=["GET"])
def converter(source, target, request):
    if is_legacy(version):
        abort(416)
    print(len(request))
    if not request:
        abort(400)
    if len(request) > 140:
        abort(413)
    return gukwok.converter.codec(source, target, request)