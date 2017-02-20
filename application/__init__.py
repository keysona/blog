from flask import Flask, render_template, request
from flask_sqlalchemy import Pagination
from .config import load_config
from .model import db, Post

PER_PAGE = 3

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # configure app
    app.config.from_object(load_config())
    app.config.from_pyfile('config.cfg', silent=True)

    if app.debug or app.testing:
        # setup DebugToolbar
        # from flask_debugtoolbar import DebugToolbarExtension
        # DebugToolbarExtension(app)
        pass

    register_db(app)
    register_blueprint(app)
    register_shell_context(app)
    register_filter(app)

    return app


def register_db(app):
    db.init_app(app)


def register_blueprint(app):
    from .blog import blog
    app.register_blueprint(blog)


def register_filter(app):
    from .utils import format_datetime
    app.jinja_env.filters['format_datetime'] = format_datetime


def register_shell_context(app):
    @app.shell_context_processor
    def make_context():
        from .model import Tag, Post, User, Category
        return dict(db=db, Post=Post, User=User, Tag=Tag, Category=Category)
