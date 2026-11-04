from cmu_cpcs_utils import testFunction

def getKthDigit(n, k):
    return abs(n) //10**k % 10

def setKthDigit(n, k, d):
    return n - getKthDigit(n,k) * 10**k + d*10**k

@testFunction
def testSetKthDigit():
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(809, 2, 0) == 9)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(0, 2, 0) == 0)
    assert(setKthDigit(0, 0, 0) == 0)

def main():
    testSetKthDigit()

main()
