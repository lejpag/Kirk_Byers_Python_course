'''
This code compares IPv6 addresses
Shortened and full notations are handled
'''

#the below line is for Python 2 compatibility
from __future__ import print_function, unicode_literals

IPV6_ADDR_1 = '2001:0db8:3c4d:0015:0000:d234:3eee:0000'
IPV6_ADDR_2 = '2001:db8:3c4d:15:0:d234:3eee:0:'
IPV6_ADDR_3 = '2001:0db8:3c4d:0015:0000:0000:1a2f:1a2b'
IPV6_ADDR_4 = '2001:db8:3c4d:15::1a2f:1a2b'

in1 = input("Enter first IPv6 address: ")
in2 = input("Enter second IPv6 address: ")

if in1 and in2:

	ip1,ip2 = in1,in2

else:
	ip1,ip2 = IPV6_ADDR_1,IPV6_ADDR_2
	print('No IP entered, we will use the below addresses:\n',ip1,'\n',ip2)

#formating for comparison
#we choose to convert ip addresses to the full notation (including zeros)

'''
Rules for IPv6 shortened notation

leading zeros can be removed in hextets
ie 0010:2:3:4:5:6:7:8 can be shortened to 10:2:3:4:5:6:7:8

a hextet full of zeros ie 0000 can be replaced by a single 0

An entire string od zeros, at least two hextets can be removed and only once
ie 1:0000:0000:4:5:6:7:8 can be shortened to 1::4:5:6:7:8
'''

#0 padding

def padding(ip):

	#hextets leading zeros padding

	hextets = ip.split(':')

	for i in range(len(hextets)):
		if len(hextets[i]) < 4 and len(hextets[i]) > 0:
			hextets[i] = (4-len(hextets[i]))*'0'+hextets[i]

	ip = ':'.join(hextets)

	#double column :: replacement with the corresponding number of zeros

	if '::' in ip:
		hextets = ip.split(':')
		while '' in hextets: hextets.remove('')
		if ip[-2:] == '::': ip = ip[:ip.index('::')] + (8-len(hextets))*':0000'
		elif ip[:2] == '::': ip = (8-len(hextets))*'0000:' + ip[ip.index('::')+2:]
		else:  ip = ip[:ip.index('::')+1] + (8-len(hextets))*'0000:'+ip[ip.index('::')+2:]


#final comparison test

ip1,ip2 = padding(ip1),padding(ip2)

if ip1 == ip2:
	print("--> Both IP addresses are equals")
else:
	print("--> IP addresses are NOT equals")

