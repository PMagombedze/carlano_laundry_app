"""
initializing the flask app
"""

from flask import Flask, render_template, url_for
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    """error handling"""
    @app.errorhandler(404)
    def clientErr(e):
        return render_template('error/404.html'), 404
    
    @app.errorhandler(500)
    def serverErr(e):
        return render_template('error/500.html'), 500

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    return app
