import os
from flask import Flask


def create_app(test_config=None):
    # Create and configure server
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'movies.db')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    # Simple hello page
    @app.route('/hello')
    def hello():
        return 'Hello world'

    from . import db
    db.init_app(app)

    from . import movies
    app.register_blueprint(movies.bp)

    # from . import blog
    # app.register_blueprint(blog.bp)
    # app.add_url_rule('/', endpoint='index')

    return app
