#! /usr/bin/env python

import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

'''
原文地址
https://www.cnblogs.com/olivertian/p/11444480.html
'''

selector = DefaultSelector()
stopped = False
urls_todo = {"/", "/1", "/2", "/3"}


class Future:
    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result = result
        for callback in self._callbacks:
            callback(self)

    def __iter__(self):
        yield self
        return self.result


def connect(sock, address):
    f = Future()
    sock.setblocking(False)
    try:
        sock.connect(address)
    except BlockingIOError:
        pass

    def on_connected():
        f.set_result(None)

    selector.register(sock.fileno(), EVENT_WRITE, on_connected)
    yield from f
    selector.unregister(sock.fileno())


def read(sock):
    f = Future()

    def on_readable():
        f.set_result(sock.recv(4096))

    selector.register(sock.fileno(), EVENT_READ, on_readable)
    chunk = yield from f
    selector.unregister(sock.fileno())
    return chunk


def read_all(sock):
    response = []
    chunk = yield from read(sock)
    while chunk:
        response.append(chunk)
        chunk = yield from read(sock)
    return b"".join(response)


class Crawler:
    def __init__(self, url):
        self.url = url
        self.response = b""

    def fetch(self):
        global stopped
        sock = socket.socket()
        yield from connect(sock, ("xkcd.com", 80))
        get = "GET {0} HTTP/1.0\r\nHost:xkcd.com\r\n\r\n".format(self.url)
        sock.send(get.encode('ascii'))
        self.response = yield from read_all(sock)
        print(self.response)
        urls_todo.remove(self.url)
        if not urls_todo:
            stopped = True


class Task:
    def __init__(self, coro):
        self._coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self, future):
        try:
            next_future = self._coro.send(None)
        except StopIteration:
            return
        next_future.add_done_callback(self.step)


def loop():
    while not stopped:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()


if __name__ == "__main__":

    if -1:
        pass
    else:

        import time
        start = time.time()
        for url in urls_todo:
            crawler = Crawler(url)
            coro = crawler.fetch()
            Task(coro)
        loop()
        print(time.time() - start)