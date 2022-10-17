#! /usr/bin/python

from scapy.all import *

dst_ip = "172.16.111.132"
src_port = RandShort()
dst_port=1084


rcv=sr1(IP(dst=dst_ip)/TCP(dport=dst_port,flags="F"),timeout=10)

if (rcv is None):
	print("This port is open or filtered with no response")
elif(rcv.haslayer(TCP)):
	if(rcv.getlayer(TCP).flags == 0x14):
		print("This port is closed")
elif(rcv.haslayer(ICMP)):
	print("This port is open or filtered with ICMP received")
