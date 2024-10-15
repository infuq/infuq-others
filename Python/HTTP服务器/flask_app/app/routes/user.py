from flask import Blueprint

user = Blueprint('user', __name__, template_folder='app/templates')

@user.route('/say', methods=['GET'])
def say():
    return 'user say'