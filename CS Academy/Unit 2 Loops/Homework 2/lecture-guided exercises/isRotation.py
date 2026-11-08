from cmu_cpcs_utils import testFunction
import math

def digitCount(n):
    if n==0:
        return 1
    return 1+math.floor(math.log10(n))

def rotate(x,delta):
    left= x//10**delta
    right=x%10**delta
    return (right*10**(digitCount(x)-delta) + left)

def isRotation(x, y):
    xDigits=digitCount(x)
    yDigits=digitCount(y)
    maxRotation=max(xDigits,yDigits)
    for delta in range(maxRotation):
        if rotate(x,delta)==y or rotate(y,delta)==x:
            return True
    return False

@testFunction
def testIsRotation():
    assert(isRotation(1234, 4123) == True)
    assert(isRotation(1234, 3412) == True)
    assert(isRotation(1234, 2341) == True)
    assert(isRotation(1234, 1234) == True)
    assert(isRotation(0, 0) == True)
    assert(isRotation(250, 25) == True)
    assert(isRotation(25, 250) == True)
    assert(isRotation(250, 502) == True)
    assert(isRotation(502, 250) == True)
    assert(isRotation(1007, 7001) == False)
    assert(isRotation(1234, 4321) == False)

def main():
    testIsRotation()

main()
