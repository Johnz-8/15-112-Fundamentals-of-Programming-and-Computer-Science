from cmu_cpcs_utils import testFunction

def rotateString(s, k):
    if k%len(s)==0:
        return s
    k%=len(s)
    right=s[k:]
    left=s[:k]
    return right+left

@testFunction
def testRotateString():
    assert(rotateString('abcd',  1) == 'bcda')
    assert(rotateString('abcd', -1) == 'dabc')
    assert(rotateString('efgh', 4) == 'efgh')
    assert(rotateString('coffee', 2) == 'ffeeco')
    assert(rotateString('112cmu', -3) == 'cmu112')
    assert(rotateString('water', -9) == 'aterw')

def main():
    testRotateString()

main()
