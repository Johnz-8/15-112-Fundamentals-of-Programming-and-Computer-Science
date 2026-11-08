from cmu_cpcs_utils import testFunction
def doShift(msg,shift):
    baseChr='a' if msg.islower() else 'A'
    numberIndex=ord(msg)-ord(baseChr)
    newNumberIndex=numberIndex+shift
    newNumberIndex=newNumberIndex%26
    return chr(newNumberIndex+ord(baseChr))
    
def encodeCaesarCipher(msg, shift):
    result=''
    for c in msg:
        if c.isalpha():
            result+=doShift(c,shift)
        else:
            result+=c
    return result

def decodeCaesarCipher(encodedMsg, shift):
    return encodeCaesarCipher(encodedMsg,-shift)

@testFunction
def testEncodeCaesarCipher():
    assert(encodeCaesarCipher('I like zoos!', 2) == 'K nkmg bqqu!')
    assert(encodeCaesarCipher('Zebra', 1) == 'Afcsb')
    assert(encodeCaesarCipher('Zebra', -1) == 'Ydaqz')
    assert(encodeCaesarCipher('I love C3PO!', -7) == 'B ehox V3IH!')
    assert(encodeCaesarCipher('Carpe Diem', 63) == 'Nlcap Otpx')
    assert(encodeCaesarCipher('', 13) == '')

@testFunction
def testDecodeCaesarCipher():
    assert(decodeCaesarCipher('J mjlf appt!', 1) == 'I like zoos!')
    assert(decodeCaesarCipher('Bgdtc', 2) == 'Zebra')
    assert(decodeCaesarCipher('Xczpy', -2) == 'Zebra')
    assert(decodeCaesarCipher('B ehox V3IH!', -7) == 'I love C3PO!')
    assert(decodeCaesarCipher('Nlcap Otpx', 63) == 'Carpe Diem')
    assert(decodeCaesarCipher('', 13) == '')

def main():
    testEncodeCaesarCipher()
    testDecodeCaesarCipher()

main()
