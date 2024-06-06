from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import final_proj.config as config

# db객체를 create_app 함수 안에서 생성하면 블루프린트와 같은 다른 모듈에서 사용할 수 없으므로 db, migrate는 create_app 함수 밖에서 생성
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__) # 플라스크 어플리케이션 생성
    app.config.from_object(config.Config)

    # ORM
    db.init_app(app) # 함수 밖에서 생성한 객체를 앱에 등록
    migrate.init_app(app, db)
    from . import models

    # 블루프린트
    from .views import main_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)

    return app
