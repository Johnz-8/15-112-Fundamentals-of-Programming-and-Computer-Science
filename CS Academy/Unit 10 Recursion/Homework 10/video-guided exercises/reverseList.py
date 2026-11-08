from cmu_cpcs_utils import testFunction

def reverseList(L):
    if L==[]:
        return []
    else:
        first=L[0]
        rest=L[1:]
        return reverseList(rest)+[first]

@testFunction
def testReverseList():
    assert(reverseList([3, 7, 4, 5]) == [5, 4, 7, 3])
    assert(reverseList(['a', 'b', 'c', 'd', 'e']) == ['e', 'd', 'c', 'b', 'a'])
    assert(reverseList([-1, 10, 5, True]) == [True, 5, 10, -1])
    assert(reverseList([1]) == [1])
    assert(reverseList([]) == [])

    # Verify that it is non-mutating 
    L = [1, 'xyz', 11, -3]
    assert(reverseList(L) == [-3, 11, 'xyz', 1])
    assert(L == [1, 'xyz', 11, -3])

def main():
    testReverseList()

main()
