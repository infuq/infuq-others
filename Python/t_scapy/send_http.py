#! /usr/bin/env python3
# -- coding: utf-8 --

from scapy.all import sr1,send,IP,ICMP,TCP,Raw
from scapy.layers.inet import *

dst_ip       = '192.168.31.132'
dst_port     = 58081
src_port     = 58082
data         = 'GET /local/checkConn HTTP/1.1\r\nHost: 192.168.31.132:58081\r\n\r\n'

def start(target_ip, target_port, data):
    try:
        # 
        pkt = IP(dst=target_ip)/TCP(dport=target_port,sport=src_port,flags="S")
        ans = sr1(pkt)
        s_seq = ans[TCP].ack
        d_seq = ans[TCP].seq + 1

        # 
        pkt = IP(dst=target_ip)/TCP(dport=target_port,sport=src_port,ack=d_seq,seq=s_seq,flags="A")
        send(pkt)
    
        # 
        pkt = IP(dst=target_ip)/TCP(dport=target_port,sport=src_port,seq=s_seq,ack=d_seq,flags=24)/data
        ans = sr1(pkt)
    except Exception as e:
        print(e)


if __name__ == '__main__':

    start(dst_ip, dst_port, data)

