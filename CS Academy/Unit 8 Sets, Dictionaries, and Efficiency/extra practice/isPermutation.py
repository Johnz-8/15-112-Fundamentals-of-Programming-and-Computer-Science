from cmu_cpcs_utils import testFunction

def isPermutation(L):
    n=len(L)
    return set(L)==set(range(n))

@testFunction
def testIsPermutation():
    assert(isPermutation([0,2,1,4,3]) == True)
    assert(isPermutation([1,3,0,4,2]) == True)
    assert(isPermutation([1,3,5,4,2]) == False)
    assert(isPermutation([1,4,0,4,2]) == False)

    # Verify that the function is nonmutating:
    L = [0,2,1,4,3]
    isPermutation(L)
    assert(L == [0,2,1,4,3])

def main():
    testIsPermutation()

main()
