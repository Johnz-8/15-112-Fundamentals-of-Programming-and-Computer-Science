from cmu_cpcs_utils import testFunction

def nQueensChecker(board):
    n = len(board)
    queenCount=0
    for row in range(n):
        for col in range(n):
            if board[row][col]:
                queenCount+=1
                if queenInRange(board, row, col):
                    return False
                    
    return queenCount==n
    
def queenInRange(board, row, col):
    n = len(board)
    directions = [(1, 1), (1, 0), (1, -1),
                 (0, 1), (0, -1),
                 (-1, 1), (-1, 0), (-1, -1)]
    for i in range(1,n):
        for drow, dcol in directions:
            newRow=row+drow*i
            newCol=col+dcol*i
            if (0<=newRow<n and 0<=newCol<n and board[newRow][newCol]):
                return True
    return False
        

@testFunction
def testNQueensChecker():
    board = [[False, True, False, False],
             [False, False, False, True],
             [True, False, False, False],
             [False, False, True, False]]
    assert(nQueensChecker(board) == True)

    board1 = [[False, False, True, False],
              [True, False, False, False],
              [False, False, False, True],
              [False, True, False, False]]
    assert(nQueensChecker(board1) == True)

    board2 = [[True, False, False],
              [False, False, True],
              [True, False, False]]
    assert(nQueensChecker(board2) == False)

    board3 = [[True, False, True],
              [False, False, False],
              [False, True, False]]
    assert(nQueensChecker(board3) == False)

    board4 = [[True, False, False],
              [False, False, True],
              [False, True, False]]
    # queens attack each other diagonally
    assert(nQueensChecker(board4) == False)

    board5 = [[True, False, False],
              [False, False, False],
              [False, True, False]]
    # has two queens instead of three
    assert(nQueensChecker(board5) == False) 

def main():
    testNQueensChecker()

main()
