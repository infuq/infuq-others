#! /usr/bin/env python
# -*- coding:utf-8 -*-

from app import create_app

app = create_app()

@app.route("/conn")
def conn():
    return '{"data": "conn success"}'


