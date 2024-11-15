from flask import Blueprint, render_template
from flask import current_app


user = Blueprint('user', __name__, template_folder='templates')

@user.route('/say', methods=['GET'])
def say():
    return 'user say'

@user.route('/index', methods=['GET'])
def index():
    data = {
        'name': 'Life'
    }
    return render_template('user/detail.html', data=data)