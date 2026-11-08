from cmu_cpcs_utils import testFunction

def interleave(L, M):
    if L==[]:
        return M
    elif M==[]:
        return L
    else:
        firstL=L[0]
        restL=L[1:]
        firstM=M[0]
        restM=M[1:]
        return [firstL]+[firstM]+interleave(restL, restM)
            

@testFunction
def testInterleave():
    assert(interleave([1, 2], [3, 4]) == [1, 3, 2, 4])
    assert(interleave([1, 2], [3, 4, 5, 6]) == [1, 3, 2, 4, 5, 6])
    assert(interleave([1, 2, 5, 6], [3, 4]) == [1, 3, 2, 4, 5, 6])
    assert(interleave([], [3, 4]) == [3, 4])
    assert(interleave([1, 2], []) == [1,2])
    assert(interleave([1, 2, 3, 4], [5, 6, 7]) == [1, 5, 2, 6, 3, 7, 4])

def main():
    testInterleave()

main()
