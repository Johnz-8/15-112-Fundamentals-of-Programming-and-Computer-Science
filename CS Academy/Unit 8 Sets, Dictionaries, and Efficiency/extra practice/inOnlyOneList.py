from cmu_cpcs_utils import testFunction

def inOnlyOneList(L, M):
    s1=set(L)
    s2=set(M)
    return sorted((s1 | s2) - (s1 & s2))

@testFunction
def testInBothLists():
    assert(inOnlyOneList([1,2,3],[3,2,4]) == [1,4])
    assert(inOnlyOneList([2,3,4],[1,2,3]) == [1,4])
    assert(inOnlyOneList([3,2,1],[4,1,2,1]) == [3,4])
    assert(inOnlyOneList([3,2,1,2],[2,2,2]) == [1,3])
    assert(inOnlyOneList([3,2,1,2],[4]) == [1,2,3,4])
    assert(inOnlyOneList([3,2,1,2],[1,3,2]) == [])

    # Verify that the function is nonmutating:
    L = [1,2,3]
    M = [3,2,4]
    inOnlyOneList(L, M)
    assert(L == [1,2,3] and M == [3,2,4])

def main():
    testInBothLists()

main()
