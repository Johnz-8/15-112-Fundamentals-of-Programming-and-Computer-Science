from cmu_cpcs_utils import testFunction

def hasConsecutiveDigits(n):
    prevDigit=None
    n=abs(n)
    while n>0:
        currentDigit=n%10
        if currentDigit==prevDigit:
            return True
        prevDigit=currentDigit
        n//=10
        
    return False

@testFunction
def testHasConsecutiveDigits():
    assert(hasConsecutiveDigits(55) == True)
    assert(hasConsecutiveDigits(1223) == True)
    assert(hasConsecutiveDigits(1232) == False)
    assert(hasConsecutiveDigits(12225) == True)
    assert(hasConsecutiveDigits(1223344) == True)
    assert(hasConsecutiveDigits(0) == False)
    assert(hasConsecutiveDigits(-1223) == True)
    assert(hasConsecutiveDigits(-1232) == False)

def main():
    testHasConsecutiveDigits()

main()
