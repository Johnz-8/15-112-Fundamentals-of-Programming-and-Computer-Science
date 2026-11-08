from cmu_cpcs_utils import testFunction

def isGray(rgb):
    r=rgb//1000000
    g=rgb//1000%1000
    b=rgb%1000
    return r==g==b

@testFunction
def testIsGray():
    assert(isGray(112112112) == True)
    assert(isGray(112112113) == False)
    assert(isGray(123195060) == False)
    assert(isGray(255255255) == True)
    assert(isGray(0) == True)
    assert(isGray(19019019) == True)
    assert(isGray(175112) == False)

def main():
    testIsGray()

main()
