from cmu_cpcs_utils import testFunction

def nonmutatingRotateList(L, n):
    left=[]
    right=[]
    n=n%len(L) if len(L)!=0 else 0
    left=L[:len(L)-n]
    right=L[len(L)-n:]
    return right + left

def mutatingRotateList(L, n):
    n=n%len(L) if len(L)!=0 else 0
    left=L[:len(L)-n]
    L.extend(left)
    for v in left:
        L.remove(v)

@testFunction
def testMutatingRotateList():
    L = [1, 2, 3, 4]
    mutatingRotateList(L, 1)
    assert(L == [4, 1, 2, 3])

    L = [4, 3, 2, 6, 5]
    mutatingRotateList(L, 2)
    assert(L == [6, 5, 4, 3, 2])

    L = [4, 3, 2, 6, 5]
    mutatingRotateList(L, 7)
    assert(L == [6, 5, 4, 3, 2])

    L = [4, 3, 2, 6, 5]
    mutatingRotateList(L, -7)
    assert(L == [2, 6, 5, 4, 3])

    L = [1, 2, 3]
    mutatingRotateList(L, 0)
    assert(L == [1, 2, 3])
    assert(mutatingRotateList(L, -1) == None)
    assert(L == [2, 3, 1])

    L = []
    mutatingRotateList(L, 2)
    assert(L == [])

@testFunction
def testNonmutatingRotateList():
    L = [1, 2, 3, 4]
    assert(nonmutatingRotateList(L, 1) == [4, 1, 2, 3])
    assert(L == [1, 2, 3, 4])

    L = [4, 3, 2, 6, 5]
    assert(nonmutatingRotateList(L, 2) == [6, 5, 4, 3, 2])
    assert(nonmutatingRotateList(L, 7) == [6, 5, 4, 3, 2])
    assert(nonmutatingRotateList(L, -7) == [2, 6, 5, 4, 3])
    assert(L == [4, 3, 2, 6, 5])

    L = [1, 2, 3]
    assert(nonmutatingRotateList(L, 0) == [1, 2, 3])
    assert(nonmutatingRotateList(L, -1) == [2, 3, 1])
    assert(L == [1, 2, 3])

    L = []
    assert(nonmutatingRotateList(L, 2) == [])


def main():
    testMutatingRotateList()
    testNonmutatingRotateList()

main()
