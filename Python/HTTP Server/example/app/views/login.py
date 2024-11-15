from flask import Blueprint, render_template
from flask import current_app


login = Blueprint('login', __name__, template_folder='app/templates/login')

@login.route('/say', methods=['GET'])
def say():
    return 'login say'