#! /usr/bin/env python
# -- coding: utf-8 --

'''
获取局域网其他主机MAC地址
'''

from scapy.all import ARP, Ether, srp
 
target_ip = '192.168.0.1/24'
 
packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target_ip)

result = srp(packet, timeout=3)[0]
 
clients = []
for sent, receieved in result:
    clients.append({'ip':receieved.psrc, 'mac':receieved.hwsrc})
 
print("Available devices in the network:")
print("IP" + " "*18 + "MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))
