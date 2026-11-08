from cmu_cpcs_utils import testFunction
import copy

def mutatingRemoveRowAndCol(L, targetRow, targetCol):
    L.pop(targetRow)
    for rowList in L:
        rowList.pop(targetCol)

def nonmutatingRemoveRowAndCol(L, targetRow, targetCol):
    M = []
    rows, cols = len(L), len(L[0])
    for row in range(rows):
        if row==targetRow:
            continue
        newrowList=[]
        for col in range(cols):
            if col==targetCol:
                continue
            newrowList.append(L[row][col])
        M.append(newrowList)
    return M

@testFunction
def testMutatingRemoveRowAndCol():
    L = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9, 10, 11, 12]]
    mutatingRemoveRowAndCol(L, 1, 2)
    assert(L == [[1,  2,  4],
                 [9, 10, 12]])

    L = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    mutatingRemoveRowAndCol(L, 0, 0)
    assert(L == [[5, 6],
                 [8, 9]])

    L = [[1, 2],
         [3, 4]]
    mutatingRemoveRowAndCol(L, 0, 1)
    assert(L == [[3]])

    L = [[1, 2, 3]]
    mutatingRemoveRowAndCol(L, 0, 1)
    assert(L == [])

@testFunction
def testNonmutatingRemoveRowAndCol():
    L = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9, 10, 11, 12]]
    assert(nonmutatingRemoveRowAndCol(L, 1, 2) == [[1,  2,  4],
                                                   [9, 10, 12]])

    L = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    assert(nonmutatingRemoveRowAndCol(L, 0, 0) == [[5, 6],
                                                   [8, 9]])

    L = [[1, 2],
         [3, 4]]
    assert(nonmutatingRemoveRowAndCol(L, 0, 1) == [[3]])

    L = [[1, 2, 3]]
    assert(nonmutatingRemoveRowAndCol(L, 0, 1) == [])

    # Verify that the function is non-mutating
    L = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9, 10, 11, 12]]
    nonmutatingRemoveRowAndCol(L, 1, 2)
    assert(L == [[1,  2,  3,  4],
                 [5,  6,  7,  8],
                 [9, 10, 11, 12]])

def main():
    testMutatingRemoveRowAndCol()
    testNonmutatingRemoveRowAndCol()

main()
