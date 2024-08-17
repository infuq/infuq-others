#!/usr/bin/env python

from scapy.all import *

def syn_flood():
    target_ip = '127.0.0.1'
    target_port = 8080
    try:
        r = sr1(IP(dst=target_ip)/TCP(dport=target_port, sport=RandShort(), seq=RandInt(), flags='S'), verbose=False)
    except Exception:
        print('error...')
        pass

if __name__ == '__main__':
    syn_flood()