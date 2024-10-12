#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
pip3 install flask
"""

from flask import Flask
from flask import request
from flask import make_response
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='172.16.52.220', port=58081)


    