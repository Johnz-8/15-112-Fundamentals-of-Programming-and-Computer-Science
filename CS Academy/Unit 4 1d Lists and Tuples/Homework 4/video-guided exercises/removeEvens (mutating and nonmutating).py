from cmu_cpcs_utils import testFunction

def mutatingRemoveEvens(L):
    i=0
    while i<len(L):
        if L[i]%2==0:
            L.pop(i)
        else:
            i+=1

def nonmutatingRemoveEvens(L):
    result=[]
    for v in L:
        if v%2==1:
            result.append(v)
    return result

@testFunction
def testMutatingRemoveEvens():
    L = [1, 2, 3, 4, 5, 6]
    mutatingRemoveEvens(L)
    assert(L == [1, 3, 5])

    L = [9, 13, -7, 17]
    mutatingRemoveEvens(L)
    assert(L == [9, 13, -7, 17])

    L = [0, -8, -12, 6, 18]
    mutatingRemoveEvens(L)
    assert(L == [])

    L = []
    mutatingRemoveEvens(L)
    assert(L == [])

    # Verify that the function is mutating
    assert(mutatingRemoveEvens(L) == None)

@testFunction
def testNonmutatingRemoveEvens():
    assert(nonmutatingRemoveEvens([1, 2, 3, 4, 5, 6]) == [1, 3, 5])
    assert(nonmutatingRemoveEvens([9, 13, -7, 17]) == [9, 13, -7, 17])
    assert(nonmutatingRemoveEvens([0, -8, -12, 6, 18]) == [])
    assert(nonmutatingRemoveEvens([]) == [])

    # Verify that the function is nonmutating
    L = [1, 2, 3]
    nonmutatingRemoveEvens(L)
    assert(L == [1, 2, 3])

def main():
    testMutatingRemoveEvens()
    testNonmutatingRemoveEvens()

main()
