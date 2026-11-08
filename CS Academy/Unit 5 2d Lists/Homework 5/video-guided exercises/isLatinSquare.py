from cmu_cpcs_utils import testFunction

def isSquareList(L):
    for v in L:
        if type(v) != list:
            return False
        if len(v) != len(L):
            return False
    return True

def hasDuplicates(L):
    for v in L:
        if L.count(v)>1:
            return True
    return False
    
def sameValues(L, M):
    return sorted(L)==sorted(M)

def isLatinSquare(L):
    if L == []:
        return False
    if not isSquareList(L):
        return False
    if hasDuplicates(L[0]):
        return False
    n=len(L[0])
    for i in range(n):
        rowList=L[i]
        colList=[L[row][i] for row in range(n)]
        if (not sameValues(L[0], rowList)) or (not sameValues(L[0], colList)):
            return False
    return True

@testFunction
def testIsLatinSquare():
    L = [[5, 7, 1],
         [1, 5, 7],
         [7, 1, 5]]
    assert(isLatinSquare(L) == True)
    # Verify that the function is non-mutating
    assert(L == [[5, 7, 1],
                 [1, 5, 7],
                 [7, 1, 5]])

    L = [[1, 5, 7],
         [5, 1, 7],
         [1, 7, 5]]
    assert(isLatinSquare(L) == False)

    L = [[1, 2, 3],
         [3, 1, 2],
         [4, 3, 1, 2]]
    assert(isLatinSquare(L) == False)

    L = [[0, 1],
         [1, 0]]
    assert(isLatinSquare(L) == True)

    L = [[1, 4],
         [2, 1]]
    assert(isLatinSquare(L) == False)

    L = [1, 2, 3]
    assert(isLatinSquare(L) == False)

    L = [[1]]
    assert(isLatinSquare(L) == True)

def main():
    testIsLatinSquare()

main()
