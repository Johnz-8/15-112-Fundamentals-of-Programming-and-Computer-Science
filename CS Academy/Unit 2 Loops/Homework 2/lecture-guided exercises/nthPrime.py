from cmu_cpcs_utils import testFunction, rounded
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

def nthPrime(n):
    count=0
    num=0
    currentPrime=0
    while count<n+1:
        if isPrime(num):
            count+=1
            currentPrime=num
        num+=1
    return currentPrime

@testFunction
def testNthPrime():
    assert(nthPrime(0) == 2)
    assert(nthPrime(1) == 3)
    assert(nthPrime(2) == 5)
    assert(nthPrime(3) == 7)
    assert(nthPrime(4) == 11)
    assert(nthPrime(5) == 13)

def main():
    testNthPrime()

main()
