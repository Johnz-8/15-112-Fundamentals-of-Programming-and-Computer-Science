from cmu_cpcs_utils import testFunction, rounded
def squareOfAllDigits(n):
    currentDigit=0
    sum=0
    while n>0:
        currentDigit=n%10
        sum+=currentDigit**2
        n//=10
    return sum
    
def isHappyNumber(n):
    while n!=1 and n!=4:
        n=squareOfAllDigits(n)
    return n==1
    
def isPrime(n):
    count=0
    for x in range(1,n+1):
        if n%x==0:
            count+=1
    return count==2
    
def isHappyPrime(n):
    return isHappyNumber(n) and isPrime(n)

def nthHappyPrime(n):
    count=-1
    num=1
    currentHappyPrime=0
    while count<n:
        if isHappyPrime(num):
            count+=1
            currentHappyPrime=num
        num+=1
    return currentHappyPrime

@testFunction
def testNthHappyPrime():
    assert(nthHappyPrime(0) == 7)
    assert(nthHappyPrime(1) == 13)
    assert(nthHappyPrime(2) == 19)
    assert(nthHappyPrime(3) == 23)
    assert(nthHappyPrime(4) == 31)
    assert(nthHappyPrime(5) == 79)

def main():
    testNthHappyPrime()

main()
