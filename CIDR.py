# Ghostcognito's CIDR distiller
# By Ghostcognito
# CIDR will be displayed after the IP address in this format [X.X.X.X]/CIDR
# The CIDR will be between 1-30
# All you need to know about IPv4 addresses NO IPv6 here.

import re

def spliter(inputIP):
    """This is used to split an IP address up so it can be used"""
    outputIP= inputIP.split(".")
    outputIPVal_1 = int(outputIP[0])
    outputIPVal_2 = int(outputIP[1])
    outputIPVal_3 = int(outputIP[2])
    outputIPVal_4 = int(outputIP[3])
    if outputIPVal_1 > 255 or outputIPVal_2 > 255 or outputIPVal_3 > 255 or outputIPVal_4 > 255:
        return(ValueError("You can't have an IP address more than 255"))
    else:
        return(outputIP)

def binary(inputIPAddr):
    """This converts the IP address into binary"""
    inputIPAddr = str(inputIPAddr)
    inputIPAddr = spliter(inputIPAddr)
    IPList = []
    if type(inputIPAddr) == list:
        for i in inputIPAddr:
            i = int(i)
            IPList.append('%0*d' % (8, int(bin(i)[2:])))
        return(IPList)
    elif type(inputIPAddr) == int:
        return('%0*d' % (8, int(bin(inputIPAddr)[2:])))
    else:
        print("Please format the input as either an IP addr\n"
              "e.g. 192.168.0.1 or as a single int e.g. 192")

def intBinary(inputIPAddr):
    """This converts IP addresses into binary and returns it as an int"""
    inputIPAddr = str(inputIPAddr)
    inputIPAddr = spliter(inputIPAddr)
    IPList = []
    for i in inputIPAddr:
        i = int(i)
        IPList.append('%0*d' % (8, int(bin(i)[2:])))

    IPList = "".join(IPList)
    IP=int(IPList)
    return(IP)

def binaryToNum(inputBinaryNum):
    """Converts a list of binary numbers to base 10 e.g.
    ['11111111', '11110000', '00000000', '00000000'] will return '255.240.0.0'"""
    subnet=[]
    # must be formated not to have any leading zeroes e.g. '01100100' won't work
    for i in inputBinaryNum:
        subnet.append(int(i,2))
    ".".join(str(i) for i in subnet)
    return(".".join(str(i) for i in subnet))

def ipClasses():
    """For a given IP will return the public IP class it falls in"""
    inputIP=input(str('Give me the IP '))
    outputIP= spliter(inputIP)
    outputIPVal_1 = int(outputIP[0])
    outputIPVal_2 = int(outputIP[1])
    outputIPVal_3 = int(outputIP[2])
    outputIPVal_4 = int(outputIP[3])
    # it must be converted to an int
    if outputIPVal_1 in range(1, 127):
        print('%s is a class A address. /8'%(inputIP))
    elif outputIPVal_1 in range(128, 192):
        print('%s is a class B address. /16'%(inputIP))
    elif outputIPVal_1 in range(192, 224):
        print('%s is a class C address. /24'%(inputIP))
    elif outputIPVal_1 in range(224, 239):
        print('%s is a class D address. N/A'%(inputIP))
    elif outputIPVal_1 in range(240, 256):
        print('%s is a class E address. N/A'%(inputIP))
    else:
        print('%s is a non classable IP address.'%(inputIP))

def ipClassesPrivate():
    """For a given private IP address will return what class it falls in"""
    inputIP = input(str('Give me the IP '))
    outputIP= spliter(inputIP)
    outputIPVal_1 = int(outputIP[0])
    outputIPVal_2 = int(outputIP[1])
    outputIPVal_3 = int(outputIP[2])
    outputIPVal_4 = int(outputIP[3])
    if outputIPVal_1 == 10 and outputIPVal_2:
        print('%s is a class A address. /8'%(inputIP))
    elif outputIPVal_1 == 127 and outputIPVal_2 in range(16, 32):
        print('%s is a class B address. /12'%(inputIP))
    elif outputIPVal_1 == 192 and outputIPVal_2 == 168:
        print('%s is a class C address. /16'%(inputIP))
    else:
        print('%s is a non classable IP address.'%(inputIP))
    

def subnetMask(TheSubnet):
    """Converts subnet masks to binary e.g. 255.255.240.0 will be
    ['11111111', '11111111', '11110000', '00000000']"""
    inputSubnet = TheSubnet
    
    inputSubnet = inputSubnet.split(".")
    subList = []
    if type(inputSubnet) == list:
        for i in inputSubnet:
            i = int(i)
            subList.append('%0*d' % (8, int(bin(i)[2:])))
        return(subList)
    elif type(inputSubnet) == int:
        return('%0*d' % (8, int(bin(inputSubnet)[2:])))

def subListMaker(TheSubnet):
    """Takes a subnet mask and returns the CIDR for that mask"""
    inputSubnetList = subnetMask(TheSubnet)
    counter = 0
    subnet = "".join(inputSubnetList)
    #subnet = int(subnet)
    for i in subnet:
        if int(i) == 1:
            counter +=1
        else:
            counter +=0
    return("/%d"%(counter))

def subCIDR(CIDR):
    """Returns the subnet mask for a given CIDR, returns the subnet mask
    prints the subnet mask in binary"""
    #CIDR = input('Give me the CIDR ')
    CIDR=str(CIDR)
    CIDR=CIDR.strip("/")
    CIDR=int(CIDR)
    CIDRList = []
    for i in range(0, CIDR):
        CIDRList.append(str(1))
    while len(CIDRList)<32:
        CIDRList.append(str(0))
    CIDRList="".join(CIDRList)
    CIDRList=re.findall('........',CIDRList)
    #print(binaryToNum(CIDRList))
    return(CIDRList)


def intSubCIDR(CIDR):
    """Returns the CIDR as an int"""
    CIDR=str(CIDR)
    CIDR=CIDR.strip("/")
    CIDR=int(CIDR)
    CIDRList = []
    for i in range(0, CIDR):
        CIDRList.append(str(1))
    while len(CIDRList)<32:
        CIDRList.append(str(0))
    CIDRList="".join(CIDRList)
    CIDR = int(CIDRList)
    return(CIDR)

def ipCIDRCombo():
    """Makes a subnet mask from an IP and the CIDR"""
    # make it so that the CIDR can be left black and defaults used instead
    IPAddr = input('Please input the ip ')
    CIDR = input('Please give the CIDR ')
    IPAddr = intBinary(IPAddr)
    CIDR = intSubCIDR(CIDR)
    IPAddrAndCIDR = IPAddr and CIDR
    IPAddrAndCIDR = str(IPAddrAndCIDR)
    formatedIPAndCIDR=re.findall('........',IPAddrAndCIDR)
    print(formatedIPAndCIDR)
    return(binaryToNum(formatedIPAndCIDR))

def isPowerOfTwo(x):
    """Checks is a number is a power of 2"""
    while(x%2==0 and x > 1):
	    x /= 2
    return(x==1)

def singleBinaryToNum(inputNum):
    """Converts a single binary number to an int"""
    inputNum = str(inputNum)
    inputNum = int(inputNum, 2)
    return(inputNum)

def howManyHostsCalc(numberOfHosts):
    """This works out the size of a subnet you will need
    for a given amount of hosts. This takes into consideration the
    subnet=n-2, you DON'T need to subtract 2 from the returned value."""
    numberOfHosts = numberOfHosts+2
    numberOfHosts = '%0*d' % (1, int(bin(numberOfHosts)[2:]))
    if isPowerOfTwo(singleBinaryToNum(numberOfHosts)) == True:
        return(numberOfHosts)
    else:
        numberOfHosts = int(numberOfHosts)
        numberOfHosts = singleBinaryToNum(numberOfHosts)*2**1
        numberOfHosts = '%0*d' % (1, int(bin(numberOfHosts)[2:]))
        numberOfHosts = str(numberOfHosts)
        numberOfHosts = list(numberOfHosts)
        listNumOfHosts=[]
        for i in range(0,len(numberOfHosts)):
            listNumOfHosts.append('0')
        listNumOfHosts[0]='1'
        listNumOfHosts = ''.join(listNumOfHosts)
        listNumOfHosts = int(listNumOfHosts)
        return(listNumOfHosts)

def howManyHostSubnet(numberOfHosts):
    """This will return the most effisient subnet
    for a given amount of hosts"""
    hostNumber = howManyHostsCalc(numberOfHosts)
    hostNumber = str(hostNumber)
    hostNumber = list(hostNumber)
    for i in hostNumber:
        if len(hostNumber) < 32:
            hostNumber.insert(0,'1')
    hostNumber = "".join(hostNumber)
    hostNumber = str(hostNumber)
    hostNumber = re.findall('........',hostNumber)
    print('You will need a subnet of %s'%binaryToNum(hostNumber))
    return(binaryToNum(hostNumber))

def howManyHostCIDR(numberOfHosts):
    hostNumber = howManyHostSubnet(numberOfHosts)
    print('You will need a CIDR of %s' % subListMaker(hostNumber))
    return(subListMaker(hostNumber))
    

def hostCalc(numberOfHosts):
    amountOfHosts=howManyHostsCalc(numberOfHosts)
    print('You will need a subnet that can support at least %s hosts'%singleBinaryToNum(amountOfHosts))
        
def subnetHostCalc():
    """Retruns how many hosts a given CIDR can support.
    You DON'T need to subtract 2 from the returned value"""
    CIDR = input('Please input the CIDR ')
    hostCount = []
    CIDRFormated = subCIDR(CIDR)
    CIDRFormated = "".join(CIDRFormated)
    CIDRFormated = CIDRFormated.strip('1')
    for i in CIDRFormated:
        hostCount.append('1')
    hostCount = "".join(hostCount)
    hostCount = int(hostCount,2)
    hostCount = hostCount - 2
    print("This CIDR can support %s hosts."%hostCount)

def subnetCalc():
    CIDR = input('Please input the CIDR ')
    CIDRFormated = subCIDR(CIDR)
    CIDRFormated = "".join(CIDRFormated)
    CIDRFormated = CIDRFormated.strip('1')
    CIDRFormated = list(CIDRFormated)
    CIDRFormated.insert(0,'1')
    CIDRFormated = "".join(CIDRFormated)
    subnetCount = int(CIDRFormated,2)
    count = subnetCount
    for i in range(0,255, subnetCount):
        print(subnetCount)
        subnetCount += count
    # Add useable range and so that it can print out for diffrnet section in the
    # octet
        
