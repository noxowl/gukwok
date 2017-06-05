#!/usr/bin/env python

from sassutils.wsgi import SassMiddleware
from gukwok.web.app import app


if __name__ == "__main__":
    app.wsgi_app = SassMiddleware(app.wsgi_app,
        {'gukwok.web': ('static/sass', 'static/css', '/static/css')}
        )
    app.run(debug=True)
