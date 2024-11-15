from flask import render_template
from flask import send_from_directory
from flask import Flask
from views.auth import auth
from views.user import user
from views.login import login
from config import ProdConfig



app = Flask(__name__)
# 注册蓝图
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(login, url_prefix='/login')
# 加载配置
app.config.from_object(ProdConfig)



@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.root_path, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', data={})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=58081)


    