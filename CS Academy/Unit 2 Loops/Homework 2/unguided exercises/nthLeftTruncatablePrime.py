from cmu_cpcs_utils import testFunction, rounded
import math
def digitCount(n):
    if n==0:
        return 1
    return 1+math.floor(math.log10(n))
    
def isPrime(n):
    if n<2:
        return False
    if n%2==0 and n>2:
        return False
    for x in range(2,math.floor(n**0.5)+1):
        if n%x==0:
            return False
    return True

def isLeftTruncatablePrime(n):
    digitsN=digitCount(n)
    if n==0:
        return False
    while n>0:
        leftMostDigit=n//10**(digitsN-1)
        if leftMostDigit==0:
            return False
        if not isPrime(n):
            return False
        n%=10**(digitsN-1)
        digitsN-=1
    return True

def nthLeftTruncatablePrime(n):
    currentLeftTruncatablePrime=None
    num=0
    count=-1
    while count<n:
        if isLeftTruncatablePrime(num):
            count+=1
            currentLeftTruncatablePrime=num
        num+=1
    return currentLeftTruncatablePrime

@testFunction
def testIsLeftTruncatablePrime():
    assert(isLeftTruncatablePrime(2) == True)
    assert(isLeftTruncatablePrime(113) == True)
    assert(isLeftTruncatablePrime(137) == True)
    assert(isLeftTruncatablePrime(1223) == True)
    assert(isLeftTruncatablePrime(0) == False)
    assert(isLeftTruncatablePrime(11) == False)
    assert(isLeftTruncatablePrime(103) == False)
    assert(isLeftTruncatablePrime(1234) == False)

@testFunction
def testNthLeftTruncatablePrime():
    assert(nthLeftTruncatablePrime(0) == 2)
    assert(nthLeftTruncatablePrime(1) == 3)
    assert(nthLeftTruncatablePrime(5) == 17)
    assert(nthLeftTruncatablePrime(10) == 53)
    assert(nthLeftTruncatablePrime(15) == 113)


def main():
    testIsLeftTruncatablePrime()
    testNthLeftTruncatablePrime()

main()
