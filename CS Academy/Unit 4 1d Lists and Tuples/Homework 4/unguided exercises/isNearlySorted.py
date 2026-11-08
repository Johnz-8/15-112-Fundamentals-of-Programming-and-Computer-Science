from cmu_cpcs_utils import testFunction
import copy

def isNearlySorted(L):
    sortedL=sorted(L)
    count=0
    result=[]
    for i in range(len(L)):
        if L[i] != sortedL[i]:
            count+=1
            result.append(i)
    if count != 2:
        return False 
    return result

@testFunction
def testIsNearlySorted():
    assert(isNearlySorted([2, 7, 5, 4]) == [1, 3])
    assert(isNearlySorted([2, 3, 1]) == False)
    assert(isNearlySorted([1, 2, 3]) == False)
    assert(isNearlySorted([-1, 1, 0, 5]) == [1, 2])
    assert(isNearlySorted([5, 6, 9, 8, 8]) == [2, 4])
    assert(isNearlySorted([2, 1]) == [0, 1])
    assert(isNearlySorted([3, 3]) == False)
    assert(isNearlySorted([2]) == False)
    assert(isNearlySorted([]) == False)

    # Verify that the function is non-mutating
    L = [2, 7, 5, 4]
    isNearlySorted(L)
    assert(L == [2, 7, 5, 4])

def main():
    testIsNearlySorted()

main()
