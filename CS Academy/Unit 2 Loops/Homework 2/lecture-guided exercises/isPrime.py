from cmu_cpcs_utils import testFunction
import math

def isPrime(n):
    if n<2:
        return False
    if n%2==0 and n>2:
        return False
    for x in range(2,math.floor(n**0.5)+1):
        if n%x==0:
            return False
    return True

@testFunction
def testIsPrime():
    assert(isPrime(1) == False)
    assert(isPrime(2) == True)
    assert(isPrime(7) == True)
    assert(isPrime(8) == False)
    assert(isPrime(9) == False)
    assert(isPrime(0) == False)
    assert(isPrime(-1) == False)
    assert(isPrime(-7) == False)

def main():
    testIsPrime()
main()
