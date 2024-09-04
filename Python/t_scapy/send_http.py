#! /usr/bin/env python
# -- coding: utf-8 --

from scapy.all import sr1,send,IP,ICMP,TCP,Raw


target_ip       = '192.168.10.9'
target_port     = 58081
data            = 'GET /local/checkConn?address=chengdu HTTP/1.1 \r\n\r\n'

def start_tcp(target_ip, target_port):
    global sport,s_seq,d_seq
    try:
        ans = sr1(IP(dst=target_ip)/TCP(dport=target_port,sport=58082,seq=1,flags='S'),verbose=False)
        sport = ans[TCP].dport
        s_seq = ans[TCP].ack
        d_seq = ans[TCP].seq + 1
        send(IP(dst=target_ip)/TCP(dport=target_port,sport=sport,ack=d_seq,seq=s_seq,flags='A'),verbose=False)
    except:
        pass

def trans_data(target_ip, target_port, data):
    # 建立TCP连接
    start_tcp(target_ip=target_ip,target_port=target_port)
    # 发起GET请求
    ans = sr1(IP(dst=target_ip)/TCP(dport=target_port,sport=sport,seq=s_seq,ack=d_seq,flags=24)/data,verbose=False)
    

if __name__ == '__main__':

    trans_data(target_ip, target_port, data)