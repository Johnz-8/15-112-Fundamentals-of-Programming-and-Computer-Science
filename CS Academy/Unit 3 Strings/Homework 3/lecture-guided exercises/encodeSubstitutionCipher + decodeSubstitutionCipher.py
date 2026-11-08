from cmu_cpcs_utils import testFunction
import string

def encodeSubstitutionCipher(msg, key):
    result=''
    for c in msg:
        if c.isalpha():
            if c.isupper():
                index=ord(c)-ord('A')
                result+=key[index]
            else:
                index=ord(c)-ord('a')
                result+=key[index].lower()
        else:
            result+=c
    return result

def decodeSubstitutionCipher(encodedMsg, key):
    result=''
    for c in encodedMsg:
        if c.isalpha():
            offset=key.find(c.upper())
            if c.isupper():
                result+=chr(ord('A')+offset)
            else:
                result+=chr(ord('a')+offset)
        else:
            result+=c
    return result

def decodeSubstitutionCipher(encodedMsg, key):
    return 0

@testFunction
def testEncodeSubstitutionCipher():
    assert(encodeSubstitutionCipher('CAB',
    'SQGYFEZXLANKJIMPURDCWTHVOB') == 'GSQ')
    assert(encodeSubstitutionCipher('Cab Z?',
    'SQGYFEZXLANKJIMPURDCWTHVOB') == 'Gsq B?')
    assert(encodeSubstitutionCipher('Hello, World!',
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'Hello, World!')
    assert(encodeSubstitutionCipher('42 - 0 = 42',
    'XHNSBMTOPQWGZDCEAVLKJYIURF') == '42 - 0 = 42')
    assert(encodeSubstitutionCipher('', 'XHNSBMTOPQWGZDCEAVLKJYIURF') == '')

@testFunction
def testDecodeSubstitutionCipher():
    assert(decodeSubstitutionCipher('GSQ',
    'SQGYFEZXLANKJIMPURDCWTHVOB') == 'CAB')
    assert(decodeSubstitutionCipher('Gsq B?',
    'SQGYFEZXLANKJIMPURDCWTHVOB') == 'Cab Z?')
    assert(decodeSubstitutionCipher('Hello, World!',
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'Hello, World!')
    assert(decodeSubstitutionCipher('42 - 0 = 42',
    'XHNSBMTOPQWGZDCEAVLKJYIURF') == '42 - 0 = 42')
    assert(decodeSubstitutionCipher('', 'XHNSBMTOPQWGZDCEAVLKJYIURF') == '')

def main():
    #testEncodeSubstitutionCipher()
    #testDecodeSubstitutionCipher()
    print(encodeSubstitutionCipher(string.ascii_uppercase,'SQGYFEZXLANKJIMPURDCWTHVOB'))
main()
