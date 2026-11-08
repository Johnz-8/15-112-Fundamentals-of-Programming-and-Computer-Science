from cmu_cpcs_utils import testFunction

def hasNoDuplicates(L):
    return len(set(L))==len(L)

@testFunction
def testHasNoDuplicates():
    assert(hasNoDuplicates([1,2,3,2]) == False)
    assert(hasNoDuplicates([1,2,3,4]) == True)
    assert(hasNoDuplicates([ ]) == True)
    assert(hasNoDuplicates([42]) == True)
    assert(hasNoDuplicates([42, 42]) == False)

    # Verify that the function is nonmutating:
    L = [1,2,3,2]
    hasNoDuplicates(L)
    assert(L == [1,2,3,2])

def main():
    testHasNoDuplicates()

main()
