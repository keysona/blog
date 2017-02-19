from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from .config import load_config
from .model import db


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # configure app
    app.config.from_object(load_config())
    app.config.from_pyfile('config.cfg', silent=True)

    if app.debug or app.testing:
        # setup DebugToolbar
        from flask_debugtoolbar import DebugToolbarExtension
        DebugToolbarExtension(app)

    register_db(app)
    register_shell_context(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app


def register_db(app):
    db.init_app(app)


def register_shell_context(app):
    @app.shell_context_processor
    def make_context():
        from .model import Tag, Post, User, Category
        return dict(db=db, Post=Post, User=User, Tag=Tag, Category=Category)
