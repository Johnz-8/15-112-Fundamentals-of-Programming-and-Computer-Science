from cmu_cpcs_utils import testFunction, rounded
import copy

def isLegalSudoku(grid):
    if len(grid)!=len(grid[0]):
        return False
    if len(grid)!=4 and len(grid)!=9:
        return False
    if not isValidRows(grid):
        return False
    if not isValidCols(grid):
        return False    
    if not isValidBlocks(grid):
        return False
    return True 

def isValidRows(grid):
    for row in grid:
        if not isValidValue(row):
            return False
    return True
    
def isValidCols(grid):
    for i in range(len(grid[0])):
        colList=[grid[row][i] for row in range(len(grid[0]))]
        if not isValidValue(colList):
            return False
    return True
    
def isValidBlocks(grid):
    n = len(grid)
    blocksize=int(n**0.5)
    for i in range(len(grid)):
        startRow=i//blocksize*blocksize
        startCol=i%blocksize*blocksize
        block=[]
        for row in range(startRow, startRow+blocksize):
            for col in range(startCol, startCol+blocksize):
                block.append(grid[row][col])
        if not isValidValue(block):
            return False
    return True

def isValidValue(L):
    n = len(L)
    for v in L:
        if type(v)!=int:
            return False
        if v<0 or v>n:
            return False
        if v>0 and L.count(v)>1:
            return False
    return True

@testFunction
def testIsLegalSudoku():
    
    okGrid1 = [
     [ 3, 0, 4, 0 ],
     [ 0, 1, 0, 2 ],
     [ 0, 4, 0, 3 ],
     [ 2, 0, 1, 0 ]
    ]
    badGrid1 = copy.deepcopy(okGrid1)
    badGrid1[3][3] = 1

    assert(isLegalSudoku(okGrid1) == True)
    assert(isLegalSudoku(badGrid1) == False)

    okGrid2 = [
     [ 3, 2, 4, 1 ],
     [ 4, 1, 3, 2 ],
     [ 1, 4, 2, 3 ],
     [ 2, 3, 1, 4 ]
    ]
    badGrid2 = copy.deepcopy(okGrid2)
    badGrid2[2][2] = 4

    assert(isLegalSudoku(okGrid2) == True)
    assert(isLegalSudoku(badGrid2) == False)

    badGrid3 = [
     [ 1, 0, 2, 0 ],
     [ 0, 2, 0, 1 ],
     [ 3, 2, 4, 0 ],
     [ 0, 4, 0, 3 ]
    ]
    assert(isLegalSudoku(badGrid3) == False)

    badGrid4 = [
     [ 1, 2, 3, 4 ],
     [ 2, 3, 4, 1 ],
     [ 3, 4, 1, 2 ],
     [ 4, 1, 2, 3 ]
    ]
    assert(isLegalSudoku(badGrid4) == False)

    #  not 4x4 or 9x9
    badGrid5 = [
     [ 3, 0, 4, 0 ],
     [ 0, 1, 0, 2 ],
     [ 0, 4, 0, 3 ]
    ]
    
    assert(isLegalSudoku(badGrid5) == False)
    
    #  contains an integer that is out of range (5)
    badGrid6 = [
     [ 3, 0, 5, 4 ],
     [ 3, 4, 1, 2 ],
     [ 2, 1, 4, 3 ],
     [ 4, 3, 2, 0 ]
    ]
    
    assert(isLegalSudoku(badGrid6) == False)

    #  contains a non-integer
    badGrid7 = [
     [ 3, 0, 4, 0 ],
     [ 0, 1, 0, 2 ],
     [ 0, 4, 0, 3 ],
     [ 2, 0, 1, 'do not crash!' ]
    ]
    
    assert(isLegalSudoku(badGrid7) == False)

    #  now test 9x9 boards
    okGrid3 = [
     [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
     [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
     [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
     [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
     [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
     [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
     [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
     [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
     [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
    ]
    badGrid8 = copy.deepcopy(okGrid3)
    badGrid8[0][0] = 7
    
    assert(isLegalSudoku(okGrid3) == True)
    assert(isLegalSudoku(badGrid8) == False)

def main():
    testIsLegalSudoku()

main()
