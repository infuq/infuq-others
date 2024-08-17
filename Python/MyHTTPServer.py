#! /usr/bin/env python
# -*- coding:utf-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

res = {'result': 'this is a test'}
host = ('127.0.0.1', 8081)


class Request(BaseHTTPRequestHandler):

    def do_GET(self):
        # 解析请求参数
        if '?' in self.path:
            data = self.path.split('?', 1)[1] + '\n'
            print(data)
            with open('./data.txt', 'ab+') as f:
                f.writelines([data.encode()])

        # 响应
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        # 允许跨域
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(res).encode())


if __name__ == '__main__':
    server = HTTPServer(host, Request)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()



