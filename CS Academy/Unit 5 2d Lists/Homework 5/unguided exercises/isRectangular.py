from cmu_cpcs_utils import testFunction

def isRectangular(L):
    rows, cols= len(L), len(L[0])
    for row in range(rows):
            if len(L[row])!= cols:
                return False
    return True

@testFunction
def testIsRectangular():
    L = [[1, 2, 3],
         [4, 5, 6]]
    assert(isRectangular(L) == True)
    L = [[1, 2],
         [4, 5, 6]]
    assert(isRectangular(L) == False)
    L = [[1, 2, 3],
         [4, 5, 6],
         [7, 8]]
    assert(isRectangular(L) == False)
    L = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9, 10, 11, 12]]
    assert(isRectangular(L) == True)

def main():
    testIsRectangular()

main()
