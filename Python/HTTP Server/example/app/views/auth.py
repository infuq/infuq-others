from flask import Blueprint, render_template
from flask import current_app


auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/say', methods=['GET'])
def say():
    return 'auth say: ' + current_app.config['DATE']

@auth.route('/index', methods=['GET'])
def index():
    data = {
        'name': 'Life'
    }
    return render_template('auth/detail.html', data=data)