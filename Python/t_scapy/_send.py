#! /usr/bin/env python
# -- coding: utf-8 --

"""
pip install scapy
或
sudo pip3 install scapy
"""

from scapy.all import sr1,send,IP,ICMP,TCP

if __name__ == '__main__':
    
    # 应用层数据
    data = 't.infuq.com'

    packet = IP(src='127.0.0.1', dst='127.0.0.1')/TCP(sport=55285, dport=8081)/data

    '''
    查看iface具体值
    C:/Users/infuq>scapy
    >>> ifaces
    '''
    # send(packet, inter=1, count=5, iface='Qualcomm QCA9377 802.11ac Wireless Adapter')
    send(packet, inter=1, count=1, iface='Software Loopback Interface 1')



