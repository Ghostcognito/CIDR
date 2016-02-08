# This is information on IP classes

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
