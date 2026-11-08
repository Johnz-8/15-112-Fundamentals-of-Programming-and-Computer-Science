from cmu_cpcs_utils import testFunction
import math
def digitCount(n):
    if n==0:
        return 1
    return 1+math.floor(math.log10(n))

def occursIn(haystack, needle):
    digitN=digitCount(needle)
    currentDigit=0
    if haystack==needle==0:
        return True
    while haystack>0:
        currentDigits=haystack%10**digitN
        if currentDigits==needle:
            return True
        haystack//=10
    return False

@testFunction
def testOccursIn():
    assert(occursIn(183742, 374) == True) 
    assert(occursIn(48372, 374) == False) 
    assert(occursIn(842092, 20) == True)
    assert(occursIn(423, 4) == True)
    assert(occursIn(423, 6) == False)
    assert(occursIn(12323, 123) == True)
    assert(occursIn(1317141, 374) == False)
    assert(occursIn(1, 1) == True)
    assert(occursIn(100, 0) == True)
    assert(occursIn(0, 0) == True)

def main():
    testOccursIn()

main()
