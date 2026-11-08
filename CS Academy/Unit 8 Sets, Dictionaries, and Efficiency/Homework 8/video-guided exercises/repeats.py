from cmu_cpcs_utils import testFunction

def repeats(L):
    seen=set()
    seenAgain=set()
    for v in L:
        if v in seen:
            seenAgain.add(v)
        seen.add(v)
    return sorted(seenAgain)

@testFunction
def testRepeats():
    assert(repeats([1,2,3,2,1]) == [1,2])
    assert(repeats([1,2,3,2,2,4]) == [2])
    assert(repeats([1,5,3,5,2,3,2,1]) == [1,2,3,5])
    assert(repeats([7,9,1,3,7,1]) == [1,7])
    assert(repeats(list(range(100))) == [ ])
    assert(repeats(list(range(100))*5) == list(range(100)))

    # Verify that the function is nonmutating:
    L = [1,2,3,2,1]
    repeats(L)
    assert(L == [1,2,3,2,1])

def main():
    testRepeats()

main()
