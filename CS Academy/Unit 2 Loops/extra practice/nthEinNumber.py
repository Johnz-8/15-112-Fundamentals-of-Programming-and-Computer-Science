from cmu_cpcs_utils import testFunction

def isEinNumber(n):
    currentEven=10
    while n>0:
        dn=n%10
        if n%2==0:
            if dn>=currentEven:
                return False
            currentEven=dn
        n//=10
    return True

def nthEinNumber(n):
    count=0
    currentEinNumber=None
    num=0
    while count<=n:
        if isEinNumber(num):
            count+=1
            currentEinNumber=num
        num+=1
    return currentEinNumber

@testFunction
def testIsEinNumber():
    assert(isEinNumber(0) == True)
    assert(isEinNumber(1) == True)
    assert(isEinNumber(2) == True)
    assert(isEinNumber(10) == True)
    assert(isEinNumber(114) == True)
    assert(isEinNumber(238) == True)
    assert(isEinNumber(317) == True)
    assert(isEinNumber(1469) == True)
    assert(isEinNumber(60) == False)
    assert(isEinNumber(22) == False)

@testFunction
def testNthEinNumber():
     assert(nthEinNumber(0) == 0)
     assert(nthEinNumber(2) == 2)
     assert(nthEinNumber(10) == 10)
     assert(nthEinNumber(99) == 114)
     assert(nthEinNumber(185) == 238)
     assert(nthEinNumber(245) == 317)
     assert(nthEinNumber(1000) == 1469)

def main():
    testIsEinNumber()
    testNthEinNumber()

main()