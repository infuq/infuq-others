#! /usr/bin/env python
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
        self.telnet = None

    def invoke(self, command):
        try:
            if self.telnet is None:
                self.telnet = telnetlib.Telnet(host=self.host, port=self.port, timeout=self.__connect_timeout)
        except socket.error as err:
            print("[host:%s port:%s] %s" % (self.host, self.port, err))
            return

        self.telnet.write(b'\n')
        self.telnet.read_until(self.__finish.encode(), timeout=self.__read_timeout)
        self.telnet.write(command.encode() + b"\n")

        recv = ''
        while str(recv).find(self.__finish) == -1:
            recv = self.telnet.read_very_eager()
        recv = recv.split("\n")[0]            
        # recv = recv.decode().split("\n")[0]
        return recv

    def close(self):
        self.telnet.close()


def main(host='127.0.0.1', port=20880):

    telnet = DubboTelnet(host, port)
    with open('1.txt') as f:
        for cmd in f.readlines():
            if cmd:
                ret = telnet.invoke(cmd)
                print(ret)
    telnet.close()


if __name__ == "__main__":
    try:
        main('127.0.0.1', 20880)
    finally:
        sys.exit()
