from flask import Flask
from database import db
from rotas import rotas_api
from config import DevConfiguration, TestConfigurarion

def create_app(config=DevConfiguration):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    app.register_blueprint(rotas_api)

    return app

def setup_db(app):
    with app.app_context():
        db.create_all()

def current_app():
    app = create_app()
    setup_db(app)
    return app

if __name__ == '__main__':
    current_app().run()