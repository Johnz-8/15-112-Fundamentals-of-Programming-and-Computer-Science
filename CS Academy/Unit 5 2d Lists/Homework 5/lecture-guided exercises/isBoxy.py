from cmu_cpcs_utils import testFunction

def isBoxy(board):
    rows, cols = len(board), len(board[0])
    uniqueValues=[]
    uniqueValues=getUniqueValues(board)
    for v in uniqueValues:
        row0, col0 = getFirstOccurrence(board, v)
        row1, col1 = getLastOccurrence(board, v)
        for row in range(rows):
            for col in range(cols):
                if board[row][col]==v:
                    if row<row0 or row>row1 or col<col0 or col>col1:
                        return False
                else:
                    if row0<=row<=row1 and col0<=col<=col1:
                        return False
    return True

def getUniqueValues(board):
    rows, cols = len(board), len(board[0])
    result=[]
    for row in range(rows):
        for col in range(cols):
            if board[row][col] not in result:
                result.append(board[row][col])
    return result

def getFirstOccurrence(board, value):
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col]==value:
                return row, col

def getLastOccurrence(board, value):
    rows, cols = len(board), len(board[0])
    for row in range(rows-1, -1, -1):
        for col in range(cols-1, -1, -1):
            if board[row][col]==value:
                return row, col
@testFunction
def testIsBoxy():
    board1 =  [ [ 1, 1, 2, 3, 3, 3 ],
                [ 1, 1, 2, 3, 3, 3 ],
                [ 1, 1, 4, 3, 3, 3 ] ]
    assert(isBoxy(board1) == True)

    board2 =  [ [ 2, 2, 3 ],
                [ 2, 2, 4 ],
                [ 1, 1, 4 ] ]
    assert(isBoxy(board2) == True)

    board3 =  [ [ 0, 1, 2, 3 ],
                [ 1, 1, 2, 3 ],
                [ 1, 1, 4, 3 ] ]
    assert(isBoxy(board3) == False) # 1 is not boxy

    board4 =  [ [ 0, 3, 3, 3 ],
                [ 0, 3, 9, 3 ],
                [ 1, 3, 3, 3 ] ]
    assert(isBoxy(board4) == False) # 3 is not boxy (due to the 9)

    board5 =  [ [ 1, 1, 2, 2 ],
                [ 1, 1, 5, 5 ],
                [ 5, 7, 5, 5 ] ]
    assert(isBoxy(board5) == False) # 5 is not boxy (see bottom-left corner)

def main():
    testIsBoxy()

main()
