from cmu_cpcs_utils import testFunction

def matrixMultiply(m1, m2):
    rows1, cols1=len(m1), len(m1[0])
    rows2, cols2=len(m2), len(m2[0])
    if cols1!=rows2:
        return None
    result=[[0 for v in range(cols2)] for v in range(rows1)]
    for row1 in range(rows1):
        rowList=m1[row1]
        for col2 in range(cols2):
            colList=[m2[row2][col2] for row2 in range(rows2)]
            sum=0
            for i in range(len(rowList)):
                sum+=rowList[i]*colList[i]
            result[row1][col2]=sum
    return result

@testFunction
def testMatrixMultiply():
    m1 = [[1, 2, 3],
          [4, 5, 6]]
    m2 = [[ 7,  8],
          [ 9, 10],
          [11, 12]]
    assert(matrixMultiply(m1, m2) == [[ 58,  64],
                                      [139, 154]])
    m1 = [[-1, 0, 1]]
    m2 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
    assert(matrixMultiply(m1, m2) == [[6, 6, 6]])

    m1 = [[1, 2, 3],
          [4, 5, 6]]
    m2 = [[1, 2, 3]]
    assert(matrixMultiply(m1, m2) == None)

def main():
    testMatrixMultiply()

main()
