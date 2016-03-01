import os, sys

os.system("clear")

print "##############################"
print "IP Tools by Jackson Walker"
print "Enter IP address and subnet mask"
print "You will then see output of class, subnet, host"
print "############################## \n"

def convertBinary(str):
	"This takes a string in TCP/IP format and returns a binary number of the TCP/IP format number"
	#### My initial idea for binary numbers to happen 
	sIpSplit = str.split('.')	#split input via the .
	for x in range (0,4):
		sIpSplit[x] = toBinary(sIpSplit[x])			
	# bIP = bin(int(ipaddress.IPv4Address('str'))) #Apparently python 3.3 on, downgraded but sounds like work for compatibilty reasons
	return sIpSplit
		
def toBinary(str):
	"string to binary number"
	iStr = int(str)
	bStr = format(iStr, '08b')
	#print('toBinary Success: ' + bStr)
	return bStr

def findClass(bIpArray):
	"Find the class of the IP Address, returns char of class"
	temp = bIpArray[0]
	cClass = "e"
	print("############################## \n")
	print "Class:",
	if(temp[0] == '0'):
		print("A")
		cClass = 'a'
	elif(temp[1] == '0'):
		print("B")
		cClass = 'b'
	elif(temp[2] == '0'):
		print("C")
		cClass = 'c'
	elif(temp[3] == '0'):
		print("D")
		cClass = 'd'
	else:
		print("Invalid IP Address")
	return cClass

################# MAIN ###################
sIP = raw_input("Please input IP address to be examined: ")
sSubnet = raw_input("Please input subnet mask for this address: ")
bIpArray = convertBinary(sIP)
bSubArray = convertBinary(sSubnet)

#Find Class
cClass = findClass(bIpArray)

#Find Domain
temp1 = bIpArray[0]
temp2 = bIpArray[1]
temp3 = bIpArray[2]
temp4 = bIpArray[3]

print "Domain:",
if(cClass == 'a'):
	print(int(temp1[1:8],2))
elif(cClass == 'b'):
	print(str(int(temp1[2:8],2)) + '.' + str(int(temp2[0:8],2)))
elif(cClass == 'c'):
	print(str(int(temp1[3:8],2)) + '.' + str(int(temp2[0:8],2)) + '.' + str(int(temp3[0:8],2)))
else:
	print "Some other class or invalid"

bSubNet = [0] * 10
#Find Subnet
print 'Subnet: ',
for x in range(0,4):
	bSubNet[x] = int(bIpArray[x],2) & int(bSubArray[x],2)
	if(x !=3):
		sys.stdout.write(str(int(bSubNet[x])) + '.')
	else:
		print(str(int(bSubNet[x])))

#Find Host Address
bHostArray = [0] * 10
print 'Host: ',
for x in range(0,4):
	bHostArray[x] = int(bIpArray[x],2) & (~int(bSubArray[x],2))
	if(x !=3):
		sys.stdout.write(str(int(bHostArray[x])) + '.')
	else:
		print(str(int(bHostArray[x])))


	
	

