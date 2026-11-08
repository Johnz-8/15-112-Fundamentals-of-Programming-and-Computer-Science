from cmu_cpcs_utils import testFunction

def getKthDigit(n, k):
    return abs(n) //10**k % 10

@testFunction
def testGetKthDigit():
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 3) == 0)
    assert(getKthDigit(1, 0) == 1)
    assert(getKthDigit(1, 1) == 0)
    assert(getKthDigit(-1, 0) == 1)
    assert(getKthDigit(-1, 1) == 0)
    assert(getKthDigit(-809, 0) == 9)

def main():
    testGetKthDigit()

main()
