from cmu_cpcs_utils import testFunction
import math

def countDigits(n):
    if n==0:
        return 1
    return 1+ math.floor(math.log10(n))

def isDuplicatedNumber(n):
    if countDigits(n) % 2 ==0:
        leftHalf = n//10**(countDigits(n)//2)
        rightHalf = n % 10**(countDigits(n)//2)
        return leftHalf == rightHalf
    else:
        return False 
        


@testFunction
def testIsDuplicatedNumber():
    assert(isDuplicatedNumber(11) == True)
    assert(isDuplicatedNumber(55) == True)
    assert(isDuplicatedNumber(123123) == True)
    assert(isDuplicatedNumber(123) == False)
    assert(isDuplicatedNumber(1221) == False)
    assert(isDuplicatedNumber(12312) == False)
    assert(isDuplicatedNumber(121212) == False)
    assert(isDuplicatedNumber(1) == False)
    assert(isDuplicatedNumber(0) == False)
    assert(isDuplicatedNumber(12345678909876543211234567890987654321) == True)

    
def main():
    testIsDuplicatedNumber()

main()
