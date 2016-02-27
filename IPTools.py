import os

os.system("clear")

print "##############################"
print "IP Tools by Jackson Walker"
print "Enter IP address and subnet mask"
print "You will then see output of class, subnet, host"
print "############################## \n"

sIP = input("Please input IP address to be examined: ")
sSubnet = input("Please input subnet mask for this address: ")


def convertBinary(str):
	"This takes a string in TCP/IP format and returns a binary number of the TCP/IP format number"
	bIpSplit = [] * 10
	sIpSplit = str.split('.')
	for x in range (0,3)
		bIpSplit[x] = toBinary(sIpSplit(x))
	
	
def toBinary(str):
	"string to binary number"
	iStr = int(str)
	return bin(iStr)
	
	
	

