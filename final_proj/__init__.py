from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import final_proj.config as config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__) # 플라스크 어플리케이션 생성
    app.config.from_object(config.Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
