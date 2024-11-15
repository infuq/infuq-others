from flask import Flask
from views.auth import auth
from views.user import user
from views.login import login


# db = SQLAlchemy()
# login_manager = LoginManager()
# login_manager.session_protection = 'string'
# login_manager.login_view = 'login'

#
# def create_app():
#     app = Flask(__name__, template_folder='app/templates')
#     # 注册蓝图
#     app.register_blueprint(auth, url_prefix='/auth')
#     app.register_blueprint(user, url_prefix='/user')
#     app.register_blueprint(login, url_prefix='/login')
#
#     # 加载配置
#     app.config.from_object("config.ProdConfig")
#
#     # db.init_app(server)
#     # login_manager.init_app(server)
#
#     return app
