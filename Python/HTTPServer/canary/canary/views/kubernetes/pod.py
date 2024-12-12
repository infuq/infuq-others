
import requests
from flask import Blueprint, request, jsonify

pod_bp = Blueprint('pod', __name__, url_prefix='/pod')


@pod_bp.route('/list_pod', methods=['GET'])
def list_pod():

    headers = {
        "Origin": "https://csnew.console.aliyun.com",

        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    data = {

    }


    response = requests.post('https://csnew.console.aliyun.com/data/call.json?path=/api/v1/namespaces/wms30-test/pods', data=data, headers=headers)

    print(response.text)



if __name__ == "__main__":
    list_pod()

