#! /usr/bin/env python
# -- coding: utf-8 --

"""
pip install scapy
"""

from scapy.all import sr1,send,IP,ICMP,TCP

# 应用层数据
data = 'TESTATE'

packet = IP(src='10.0.0.3', dst='10.0.0.6')/TCP(sport=12345, dport=8000)/data

'''
查看iface具体值
C:/Users/infuq>scapy
>>> ifaces
'''
send(packet, inter=1, count=5, iface='Qualcomm QCA9377 802.11ac Wireless Adapter')


