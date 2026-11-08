from cmu_cpcs_utils import testFunction

def isKingsTour(board):
    rows, cols=len(board), len(board[0])
    startRow, startCol=findStart(board)
    if startRow==None:
        return False
    for _ in range(rows*cols-1):
        row, col = kingsMove(board, startRow, startCol)
        if row!=None:
            startRow=row
            startCol=col
        else:
            return False
    return True

def findStart(board):
    rows, cols=len(board), len(board[0])
    startRow, startCol= None, None
    for row in range(rows):
        for col in range(cols):
            if board[row][col]==1:
                startRow, startCol=row, col
    return startRow, startCol
    
def kingsMove(board, startRow, startCol):
    rows, cols=len(board), len(board[0])
    drows=[-1, 0, 1]
    dcols=[-1, 0 ,1]
    for drow in drows:
        for dcol in dcols:
            if (drow, dcol)!=(0,0):
                row=startRow+drow
                col=startCol+dcol
                if 0<=row<rows and 0<=col<cols and board[row][col]==board[startRow][startCol]+1:
                    return row, col
    return None, None

@testFunction
def testIsKingsTour():
    board = [[1, 5, 6],
             [4, 2, 7],
             [3, 8, 9]]
    assert(isKingsTour(board) == True)

    board = [[3, 2, 1],
             [7, 4, 8],
             [6, 5, 9]]
    assert(isKingsTour(board) == False)

    board = [[3, 2, 1],
             [6, 4, 0],
             [5, 7, 8]]
    assert(isKingsTour(board) == False)

    board = [[ 7,  8,  9, 10],
             [ 6,  3,  2, 11],
             [ 4,  5,  1, 12],
             [16, 15, 14, 13]]
    assert(isKingsTour(board) == True)

def main():
    testIsKingsTour()

main()
