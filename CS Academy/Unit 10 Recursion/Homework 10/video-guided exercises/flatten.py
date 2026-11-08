from cmu_cpcs_utils import testFunction

def flatten(L):
    if L==[]:
        return []
    else:
        first=L[0]
        rest=L[1:]
        if isinstance(first, list):
            return flatten(first)+flatten(rest)
        else:
            return [first]+flatten(rest)
@testFunction
def testFlatten():
    assert(flatten([1, [2]]) == [1, 2])
    assert(flatten([1, 2, [3, [4, 5], 6], 7]) == [1, 2, 3, 4, 5, 6, 7])
    assert(flatten([[2, 3], [[4]], 5]) == [2, 3, 4, 5])
    assert(flatten([[2, [[]]], 'wow', [True]]) == [2, 'wow', True])
    assert(flatten([]) == [])
    assert(flatten([[]]) == [])
    assert(flatten([3]) == [3])
    assert(flatten([[[3]]]) == [3])

def main():
    testFlatten()

main()
