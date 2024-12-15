from flask import Blueprint, request, jsonify, current_app
from sqlalchemy import text
import re
import json

from canary.core.extensions import db

area_bp = Blueprint('area', __name__, url_prefix='/area')


@area_bp.route('/search', methods=['POST'])
def search():
    keyword = request.json.get('keyword')
    curPage = request.json.get('curPage')

    # 判断是否数值
    matcher = re.match(r'^\d+$', keyword)
    if matcher:
        return search_by_code(keyword, curPage)
    else:
        return search_by_short_name(keyword, curPage)


def search_by_code(keyword, curPage):
    sql = "SELECT COUNT(*) AS total FROM (SELECT COUNT(*) FROM area WHERE code LIKE '%s' GROUP BY `code`,short_name,`name`,`level`) AS t"

    sql = sql % ('%' + keyword + '%')
    sql = text(sql)
    cursor = db.session.execute(statement=sql, params={}, bind_arguments={
        "bind": db.get_engine(bind_key="db1")
    })
    rows = cursor.mappings().all()
    total = rows[0]['total']

    areaList = []
    if total > 0:
        sql = "SELECT `code`,short_name,`name`,`level` FROM area WHERE code LIKE '%s' GROUP BY `code`,short_name,`name`,`level` LIMIT %s, %s"
        sql = sql % ('%' + keyword + '%', (curPage - 1) * 10, 10)
    else:
        response = {
            'areaList': areaList,
            'total': total
        }

        return jsonify(response)

    sql = text(sql)
    cursor = db.session.execute(statement=sql, params={
    }, bind_arguments={
        "bind": db.get_engine(bind_key="db1")
    })
    rows = cursor.mappings().all()
    for row in rows:
        data = {
            "code": row['code'],
            "shortName": row['short_name'],
            "name": row['name'],
            "level": row['level'],
        }
        areaList.append(data)

    response = {
        'areaList': areaList,
        'total': total
    }

    return jsonify(response)


def search_by_short_name(keyword, curPage):

    sql = "SELECT COUNT(*) AS total FROM (SELECT COUNT(*) FROM area WHERE short_name LIKE '%s' GROUP BY `code`,short_name,`name`,`level`) AS t"


    sql = sql % ('%' + keyword + '%')
    sql = text(sql)
    cursor = db.session.execute(statement=sql, params={}, bind_arguments={
        "bind": db.get_engine(bind_key="db1")
    })
    rows = cursor.mappings().all()
    total = rows[0]['total']

    areaList = []
    if total > 0:
        sql = "SELECT `code`,short_name,`name`,`level` FROM area WHERE short_name LIKE '%s' GROUP BY `code`,short_name,`name`,`level` LIMIT %s, %s"
        sql = sql % (('%' + keyword + '%'), (curPage - 1) * 10, 10)
    else:
        response = {
            'areaList': areaList,
            'total': total
        }

        return jsonify(response)

    sql = text(sql)
    cursor = db.session.execute(statement=sql, params={
    }, bind_arguments={
        "bind": db.get_engine(bind_key="db1")
    })
    rows = cursor.mappings().all()
    for row in rows:
        data = {
            "code": row['code'],
            "shortName": row['short_name'],
            "name": row['name'],
            "level": row['level'],
        }
        areaList.append(data)

    response = {
        'areaList': areaList,
        'total': total
    }

    return jsonify(response)



@area_bp.route('/detail', methods=['POST'])
def detail():
    code = request.json.get('code')
    shortName = request.json.get('shortName')

    sql = "SELECT * FROM area WHERE code = '%s' AND short_name = '%s'"
    sql = sql % (code,shortName)

    sql = text(sql)
    cursor = db.session.execute(statement=sql, params={
    }, bind_arguments={
        "bind": db.get_engine(bind_key="db1")
    })
    rows = cursor.mappings().all()

    area = {
        "shortCode": rows[0]['short_code'],
        "code": rows[0]['code'],
        "shortName": rows[0]['short_name'],
        "name": rows[0]['name'],
        "level": rows[0]['level']
    }
    all_year = []
    for row in rows:
        all_year.append(row['year'])
    area['allYear'] = all_year

    return jsonify(area)



@area_bp.route('/tree', methods=['POST'])
def tree():
    year = request.json.get('year')

    directory = current_app.root_path
    file = f"{directory}/views/area/data/{year}.json"

    with open(file, mode='r', encoding='utf8') as f:
        data = f.read()
        data = data.replace("'", "\"")
        return json.loads(data)

