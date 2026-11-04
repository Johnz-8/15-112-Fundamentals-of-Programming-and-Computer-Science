from cmu_cpcs_utils import testFunction
import math

def closestEven(n):
    lowerInt=math.floor(n)
    higherInt=lowerInt+1
    if lowerInt%2==0:
        return lowerInt
    else:
        return higherInt

@testFunction
def testClosestEven():
    assert(closestEven(0) == 0)
    assert(closestEven(11) == 12)
    assert(closestEven(12) == 12)
    assert(closestEven(13) == 14)
    assert(closestEven(1.01) == 2)
    assert(closestEven(2.99) == 2)
    assert(closestEven(-11) == -10)
    assert(closestEven(-12) == -12)
    assert(closestEven(-13) == -12)
    assert(type(closestEven(1)) == int)
    assert(type(closestEven(2.99)) == int)

def main():
    testClosestEven()

main()
