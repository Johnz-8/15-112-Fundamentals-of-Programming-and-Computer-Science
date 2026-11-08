from cmu_cpcs_utils import testFunction
import math

def digitCountMapInRange(lo, hi):
    if lo>hi:
        return {}
    else:
        result=digitCountMapInRange(lo+1, hi)
        addDigitsToMap(result, lo)
        return result

def addDigitsToMap(countMap, n):
    n=abs(n)
    if n<10:
        countMap[n]=countMap.get(n,0)+1
        return countMap
    else:
        last=n%10
        rest=n//10
        countMap=addDigitsToMap(countMap, rest)
        countMap[last]=countMap.get(last,0)+1
        return countMap
    
@testFunction
def testDigitCountMapInRange():
    assert(digitCountMapInRange(9, 12) == {0: 1, 1: 4, 2: 1, 9:1})
    assert(digitCountMapInRange(8, 9) == {8: 1, 9: 1})
    assert(digitCountMapInRange(-1, 3) == {0: 1, 1: 2, 2: 1, 3: 1})
    assert(digitCountMapInRange(20, 22) == {0: 1, 1: 1, 2: 4})
    assert(digitCountMapInRange(12, 9) == dict())

def main():
    testDigitCountMapInRange()

main()
