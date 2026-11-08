from cmu_cpcs_utils import testFunction
import math

def digitCount(n):
    n=abs(n)
    if (n==0):
        return 1
    return 1+math.floor(math.log10(n))

@testFunction
def testDigitCount():
    assert(digitCount(1) == 1)
    assert(digitCount(2) == 1)
    assert(digitCount(9) == 1)
    assert(digitCount(10) == 2)
    assert(digitCount(11) == 2)
    assert(digitCount(1000) == 4)
    assert(digitCount(0) == 1)
    assert(digitCount(-1) == 1)
    assert(digitCount(-1000) == 4)

def main():
    testDigitCount()

main()
