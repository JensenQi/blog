from flask import Flask, g, request
from flask.json import JSONEncoder
from datetime import datetime
from flask.ext.login import LoginManager
from models import DBSession
from datetime import datetime
from models import Log
from config import SECRET_KEY


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, datetime):
                return obj.strftime("%Y-%m-%d %H:%M:%S")
        except TypeError:
            pass
        else:
            return list(iter(obj))
        return JSONEncoder.default(self, obj)


login_manager = LoginManager()
login_manager.session_protection = 'strong'


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.json_encoder = CustomJSONEncoder
    app.config['SECRET_KEY'] = SECRET_KEY
    login_manager.init_app(app)

    @app.before_request
    def open_connect():
        g.session = DBSession()
        g.session.add(Log(ip=request.remote_addr, url=request.url, create_time=datetime.now()))
        g.session.commit()

    @app.teardown_request
    def close_connect(exception):
        session = getattr(g, 'session', None)
        if session is not None:
            session.close()

    @login_manager.user_loader
    def load_user(user_id):
        from models import User
        session = getattr(g, 'session', None)
        return session.query(User).filter_by(id=user_id).first()

    from .article import article
    from .user import user
    app.register_blueprint(article, url_prefix='/api/article')
    app.register_blueprint(user, url_prefix='/api/user')
    return app
