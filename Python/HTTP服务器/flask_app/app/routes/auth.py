from flask import Blueprint, render_template
from flask import current_app


auth = Blueprint('auth', __name__, template_folder='app/templates/user')

@auth.route('/say', methods=['GET'])
def say():
    # 读取配置文件内容
    return 'auth say: ' + current_app.config['DATE']

@auth.route('/index', methods=['GET'])
def index():
    data = {
        'name': 'Life'
    }
    return render_template('t.html', data=data)    