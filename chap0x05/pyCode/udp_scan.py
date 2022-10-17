#! /usr/bin/python

from scapy.all import *

dst_ip = "172.16.111.132"
src_port = RandShort()
dst_port=53


rcv=sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=10)

if (rcv is None):
	print("This port is open ,closed or filtered with no response")
elif(rcv.haslayer(UDP)):
	print("This port is open")
elif(rcv.haslayer(ICMP)):
	print("This port is closed")
