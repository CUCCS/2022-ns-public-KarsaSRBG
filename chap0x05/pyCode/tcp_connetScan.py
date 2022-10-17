#! /usr/bin/python

from scapy.all import *

dst_ip = "172.16.111.132"
dst_port=1084

#pkts=ans
pkts = sr1(IP(dst=dst_ip) / TCP(dport=1084, flags="S"), timeout=1)
if pkts is None:
	print("This port is filtered")
elif(pkts.haslayer(TCP)):
	if(pkts.getlayer(TCP).flags == 0x12):#0x12==syn/ack
		sr1(IP(dst=dst_ip) / TCP(dport=1084, flags="AR"), timeout=1)
		print("This port is open")
	elif (pkts.getlayer(TCP).flags == 0x14):#0x14==rst/ack
		sr1(IP(dst=dst_ip) / TCP(dport=1084, flags="R"), timeout=1)
		print("This port is closed")