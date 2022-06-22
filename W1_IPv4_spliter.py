'''
This program reads an IPv4 address and displays its octets in decimal, binary, hex
'''
#below statement is for Python 2 compatibility
from __future__ import print_function

#below try/except statement is also for Python 2 compatibility
try:
	ip_addr = raw_input("Please enter an IP address: ")

except NameError:

	ip_addr = input("Please enter an IP address: ")

#lists creation for the final display
column_labels  = ["OCTET "+str(i) for i in range(1,5)]

octets = [int(octet) for octet in ip_addr.split('.')] 

octets_bin = [bin(octet)[2:] for octet in octets]
octets_hex = [hex(octet)[2:].upper() for octet in octets]

print("\n")
print("- "*40)
print("{:5}{:^20}{:^20}{:^20}{:^20}".format("",*column_labels))
print("{:5}{:^20}{:^20}{:^20}{:^20}".format("DEC",*octets))
print("{:5}{:^20}{:^20}{:^20}{:^20}".format("BIN",*octets_bin))
print("{:5}{:^20}{:^20}{:^20}{:^20}".format("HEX",*octets_hex))
print("- "*40)
print("\n")
