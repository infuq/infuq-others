#! /usr/bin/env python

import pickle

class Seria(object):

    def __init__(self, addr, year):
        self.addr = addr
        self.year = year

    def keys(self):
        return ['addr', 'year']

    def __getitem__(self, item):
        return getattr(self, item)



if __name__ == '__main__':
    seria = Seria('江苏', 2021)

    d = pickle.dumps(seria)
    obj = pickle.loads(d)
    print(obj.addr)














