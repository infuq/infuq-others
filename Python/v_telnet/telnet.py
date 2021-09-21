#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import telnetlib
import sys


class DubboTelnet(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.__connect_timeout = 10
        self.__read_timeout = 10
        self.__encoding = 'utf-8'
        self.__finish = 'dubbo>'

    def invoke(self, command):
        print(command)
        pass
        try:
            telnet = telnetlib.Telnet(host=self.host, port=self.port, timeout=self.__connect_timeout)
        except socket.error as err:
            print("[host:%s port:%s] %s" % (self.host, self.port, err))
            return

        # 触发Dubbo提示符
        telnet.write(b'\n')
        # 执行命令
        telnet.read_until(self.__finish.encode(), timeout=self.__read_timeout)
        telnet.write(command.encode() + b"\n")
        # 获取结果
        data = ''
        while str(data).find(self.__finish) == -1:
            data = telnet.read_very_eager()
        data = data.decode().split("\n")[0]
        telnet.close()
        return data


def main(host='127.0.0.1', port=20880):

    conn = DubboTelnet(host, port)
    cmd = 'invoke ....'
    ret = conn.invoke(cmd)
    print(ret)


if __name__ == "__main__":
    try:
        main('127.0.0.1', 20880)
    finally:
        sys.exit()
