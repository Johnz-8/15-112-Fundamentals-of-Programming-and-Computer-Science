from cmu_cpcs_utils import testFunction

def permutations(L):
    if L==[]:
        return [[]]
    else:
        result=[]
        first=L[0]
        rest=L[1:]
        smallerPermutations=permutations(rest)
        for i in range(len(smallerPermutations)):
            for j in range(len(smallerPermutations[0])+1):
                result.append(smallerPermutations[i][:j]+[first]+smallerPermutations[i][j:])

        return sorted(result)

@testFunction
def testPermutations():
    assert(permutations([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], 
                                       [2, 1, 3], [2, 3, 1], 
                                       [3, 1, 2], [3, 2, 1]])
    assert(permutations([3, 1]) == [[1, 3], [3, 1]])
    assert(permutations([1]) == [[1]])
    assert(permutations([]) == [[]])

def main():
    testPermutations()

main()
