# Ghostcognito's CIDR distiller
# By Ghostcognito
# CIDR will be displayed after the IP address in this format [X.X.X.X]/CIDR
# The CIDR will be between 1-30

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
    """Converts binary numbers to base 10"""
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
        print('%s is a class A address.'%(inputIP))
    elif outputIPVal_1 in range(128, 192):
        print('%s is a class B address.'%(inputIP))
    elif outputIPVal_1 in range(192, 224):
        print('%s is a class C address.'%(inputIP))
    elif outputIPVal_1 in range(240, 255):
        print('%s is a class D address.'%(inputIP))
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
        print('%s is a class A address.'%(inputIP))
    elif outputIPVal_1 == 127 and outputIPVal_2 in range(16, 31):
        print('%s is a class B address.'%(inputIP))
    elif outputIPVal_1 == 192 and outputIPVal_2 == 168:
        print('%s is a class C address.'%(inputIP))
    else:
        print('%s is a non classable IP address.'%(inputIP))
    

def subnetMask():
    """Converts subnet masks to binary e.g. 255.255.240.0 will be
    ['11111111', '11111111', '11110000', '00000000']"""
    inputSubnet = input('Enter the subnet ')
    
    inputSubnet = inputSubnet.split(".")
    subList = []
    if type(inputSubnet) == list:
        for i in inputSubnet:
            i = int(i)
            subList.append('%0*d' % (8, int(bin(i)[2:])))
        return(subList)
    elif type(inputSubnet) == int:
        return('%0*d' % (8, int(bin(inputSubnet)[2:])))

def subListMaker():
    """Takes a subnet mask and returns the CIDR for that mask"""
    inputSubnetList = subnetMask()
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
    print(binaryToNum(CIDRList))
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


def howManyHosts(numberOfHosts):
    """This will work out the subnets for a given amount of hosts"""
    

