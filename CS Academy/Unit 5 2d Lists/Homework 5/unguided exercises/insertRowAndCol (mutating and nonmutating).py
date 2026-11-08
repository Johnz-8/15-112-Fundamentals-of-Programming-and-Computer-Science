from cmu_cpcs_utils import testFunction

def mutatingInsertRowAndCol(L, row, col, val):
    rows, cols= len(L), len(L[0])
    L.insert(row,[])
    for i in range(rows+1):
        for j in range(cols+1):
            if i==row or j==col:
                L[i].insert(j,val)

def nonmutatingInsertRowAndCol(L, row, col, val):
    rows, cols= len(L), len(L[0])
    result=[]
    for i in range(rows):
        rowList=[v for v in L[i]]
        result.append(rowList)
    result.insert(row,[])
    for i in range(rows+1):
        for j in range(cols+1):
            if i==row or j==col:
                result[i].insert(j,val)
    return result

@testFunction
def testMutatingInsertRowAndCol():
    L = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9, 10, 11, 12]]
    mutatingInsertRowAndCol(L, 1, 2, 42)
    assert(L == [[ 1,  2, 42,  3,  4],
                 [42, 42, 42, 42, 42],
                 [ 5,  6, 42,  7,  8],
                 [ 9, 10, 42, 11, 12]])

    L = [[1, 2, 3],
         [4, 5, 6]]
    mutatingInsertRowAndCol(L, 0, 0, 5)
    assert(L == [[5, 5, 5, 5],
                 [5, 1, 2, 3],
                 [5, 4, 5, 6]])

    L = [[1, 2, 3],
         [4, 5, 6]]
    mutatingInsertRowAndCol(L, 1, 3, 5)
    assert(L == [[1, 2, 3, 5],
                 [5, 5, 5, 5],
                 [4, 5, 6, 5]])

@testFunction
def testNonmutatingInsertRowAndCol():
    L = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9, 10, 11, 12]]
    assert(nonmutatingInsertRowAndCol(L, 1, 2, 42) == [[ 1,  2, 42,  3,  4],
                                                       [42, 42, 42, 42, 42],
                                                       [ 5,  6, 42,  7,  8],
                                                       [ 9, 10, 42, 11, 12]])

    L = [[1, 2, 3],
         [4, 5, 6]]
    assert(nonmutatingInsertRowAndCol(L, 0, 0, 5) == [[5, 5, 5, 5],
                                                      [5, 1, 2, 3],
                                                      [5, 4, 5, 6]])

    L = [[1, 2, 3],
         [4, 5, 6]]
    assert(nonmutatingInsertRowAndCol(L, 1, 3, 5) == [[1, 2, 3, 5],
                                                      [5, 5, 5, 5],
                                                      [4, 5, 6, 5]])

    # Verify that the function is non-mutating
    L = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9, 10, 11, 12]]
    nonmutatingInsertRowAndCol(L, 1, 2, 42)
    assert(L == [[1,  2,  3,  4],
                 [5,  6,  7,  8],
                 [9, 10, 11, 12]])

def main():
    testMutatingInsertRowAndCol()
    testNonmutatingInsertRowAndCol()

main()
