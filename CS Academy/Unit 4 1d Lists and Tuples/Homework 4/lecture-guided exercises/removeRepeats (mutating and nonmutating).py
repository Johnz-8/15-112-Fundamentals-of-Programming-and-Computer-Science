from cmu_cpcs_utils import testFunction

def mutatingRemoveRepeats(L):
    i=0
    while i<len(L):
        if L[i] in L[:i]:
            L.pop(i)
        else:
            i+=1

def nonmutatingRemoveRepeats(L):
    result=[]
    for i in range(len(L)):
        if L[i] not in L[:i]:
            result.append(L[i])
    return result

@testFunction
def testMutatingRemoveRepeats():
    L = [1, 5, 2, 2, 4, 4, 2]
    mutatingRemoveRepeats(L)
    assert(L == [1, 5, 2, 4])

    L = [-2, 15, -2, 3]
    mutatingRemoveRepeats(L)
    assert(L == [-2, 15, 3])

    L = [1, 1, 1]
    mutatingRemoveRepeats(L)
    assert(L == [1])

    L = [1, 9, 5]
    mutatingRemoveRepeats(L)
    assert(L == [1, 9, 5])

    L = []
    mutatingRemoveRepeats(L)
    assert(L == [])

    assert(mutatingRemoveRepeats(L) == None)

@testFunction
def testNonmutatingRemoveRepeats():
    assert(nonmutatingRemoveRepeats([1, 5, 2, 2, 4, 4, 2]) == [1, 5, 2, 4])
    assert(nonmutatingRemoveRepeats([-2, 15, -2, 3]) == [-2, 15, 3])
    assert(nonmutatingRemoveRepeats([1, 1, 1]) == [1])
    assert(nonmutatingRemoveRepeats([1, 9, 5]) == [1, 9, 5])
    assert(nonmutatingRemoveRepeats([]) == [])

    # Verify that the function is nonmutating:
    L = [1, 2, 2, 3, 4, 4]
    nonmutatingRemoveRepeats(L)
    assert(L == [1, 2, 2, 3, 4, 4])

def main():
    testMutatingRemoveRepeats()
    testNonmutatingRemoveRepeats()

main()
