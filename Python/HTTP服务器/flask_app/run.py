#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
pip3 install Flask
"""

import os
from flask import Flask, render_template
from flask import send_from_directory
from app.routes.auth import auth
from app.routes.user import user

app = Flask(__name__, template_folder='app/templates')
app.config.from_pyfile('app/config/config.py')

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(user, url_prefix='/user')


@app.route('/favicon.ico')#设置icon
def favicon():
    return send_from_directory(app.root_path, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', data={})    


if __name__ == '__main__':
    # print(app.root_path)
    app.run(host='192.168.10.9', port=58081)


    