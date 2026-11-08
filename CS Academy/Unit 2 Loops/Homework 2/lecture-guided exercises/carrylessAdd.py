from cmu_cpcs_utils import testFunction
import math
def getKthDigit(n,k):
    return (n//10**k%10)

def setKthDigit(n,k,d):
    currentDigit=getKthDigit(n,k)
    return n-currentDigit*10**k+d*10**k
    
def digitCount(n):
    if n == 0:
        return 1
    return 1+math.floor(math.log10(n))
    
def carrylessAdd(x, y):
    sum=0
    dx=0
    dy=0
    for k in range(max(digitCount(x),digitCount(y))):
        dx=getKthDigit(x,k)
        dy=getKthDigit(y,k)
        dsum=(dx+dy)%10
        sum+=dsum*10**k
    return sum

@testFunction
def testCarrylessAdd():
    assert(carrylessAdd(8, 7) == 5)
    assert(carrylessAdd(785, 376) == 51)
    assert(carrylessAdd(0, 325) == 325)
    assert(carrylessAdd(30, 873) == 803)
    assert(carrylessAdd(873, 30) == 803)
    assert(carrylessAdd(100, 11) == 111)

def main():
    testCarrylessAdd()

main()
