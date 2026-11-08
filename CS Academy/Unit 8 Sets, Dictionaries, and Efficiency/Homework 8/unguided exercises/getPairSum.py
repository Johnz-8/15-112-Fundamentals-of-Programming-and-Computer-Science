from cmu_cpcs_utils import testFunction
import copy

def getPairSum(L, target):
    seen=set()
    for value in L:
        if (target-value) in seen:
            return (value, target-value)
        seen.add(value)

# This helper function is used by the test function below
def isPairSum(L, target, pair):
    L = copy.copy(L)
    # Check that the pair is a tuple of length 2
    if type(pair) != tuple or len(pair) != 2: return False
    n1, n2 = pair
    # Check that the sum of the pair equals the target
    if n1 + n2 != target: return False
    # Check that both elements are in the list
    if n1 not in L: return False
    L.remove(n1)
    return n2 in L

@testFunction
def testGetPairSum():
    L = [5, 2]
    target = 7
    pair = getPairSum(L, target)
    assert(isPairSum(L, target, pair))

    L = [10, -1, 1, -8, 3]
    target = 2
    pair = getPairSum(L, target)
    assert(isPairSum(L, target, pair))

    L = [10, -1, 1, -8, 3, 1]
    target = 2
    pair = getPairSum(L, target)
    assert(isPairSum(L, target, pair))

    L = [3, 3]
    target = 6
    pair = getPairSum(L, target)
    assert(isPairSum(L, target, pair))

    L = [2, 4, 10, 7, 5, -1]
    target = 12
    pair = getPairSum(L, target)
    assert(isPairSum(L, target, pair))

    assert(getPairSum([1, 0, 3], 2) == None)
    assert(getPairSum([10, -1, 1, -8, 3, 1], 10) == None)
    assert(getPairSum([], 0) == None)

def main():
    testGetPairSum()

main()
