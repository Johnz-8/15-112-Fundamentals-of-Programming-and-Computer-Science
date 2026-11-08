from cmu_cpcs_utils import testFunction

def inBothLists(L, M):
    s= set(L) & set(M)
    return sorted(s)

@testFunction
def testInBothLists():
    assert(inBothLists([1,2,3],[3,2,4]) == [2,3])
    assert(inBothLists([3,2,1],[4,1,2,1]) == [1,2])
    assert(inBothLists([3,2,1,2],[2,2,2]) == [2])
    assert(inBothLists([1,2,3],[4,5,6,1]) == [1])
    assert(inBothLists([3,2,1,2],[4]) == [])

    # Verify that the function is nonmutating:
    L = [1,2,3]
    M = [3,2,4]
    inBothLists(L, M)
    assert(L == [1,2,3] and M == [3,2,4])

def main():
    testInBothLists()

main()
