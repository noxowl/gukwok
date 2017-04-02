"""mod: 'gukwok.web.app'

"""

from flask import Flask, current_app, abort, request, render_template

import gukwok.converter 


app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    """gukwok index page"""
    return render_template('index.html')

@app.route('/api/<source>/<target>/<request>', methods=["GET"])
def converter(source, target, request):
    return gukwok.converter.codec(source, target, request)