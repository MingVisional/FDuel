"""生成flask_app"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import dbConfig, SECRET_KEY


db = SQLAlchemy()


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = SECRET_KEY
    # 链接mysql
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@%s:%d/%s' \
                                            % (dbConfig['user'],
                                               dbConfig['password'],
                                               dbConfig['host'],
                                               dbConfig['port'],
                                               dbConfig['database'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.url_map.strict_slashes = False

    db.init_app(app)
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/')
    print(api_blueprint.register_blueprint)
    return app
