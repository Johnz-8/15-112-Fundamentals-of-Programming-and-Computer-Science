from cmu_cpcs_utils import testFunction

def wordSearch(board, word):
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == word[0]:
                if findDirection(board, word, row, col):
                    return True
    return False

def findDirection(board, word, row, col):
    rows, cols = len(board), len(board[0])
    drows = [-1, 0, 1]
    dcols = [-1, 0, 1]
    for drow in drows:
        for dcol in dcols:
            if drow==dcol==0:
                continue
            if findWord(board, word, row, col, drow, dcol):
                return True
    return False

def findWord(board, word, row, col, drow, dcol):
    rows, cols = len(board), len(board[0])
    for i in range(len(word)):
        if (row+drow*i>=rows or
        row+drow*i<0 or
        col+dcol*i>=cols or
        col+dcol*i<0 or
        board[row+drow*i][col+dcol*i]!=word[i]):
            return False
    return True
@testFunction
def testWordSearch():
    board = [ [ 'd', 'o', 'g' ],
              [ 't', 'a', 'c' ],
              [ 'w', 'a', 't' ],
              [ 'u', 'r', 'b' ] ]
    assert(wordSearch(board, 'dog') == True)
    assert(wordSearch(board, 'cat') == True)
    assert(wordSearch(board, 'bat') == True)
    assert(wordSearch(board, 'tab') == True)
    assert(wordSearch(board, 'wag') == True)
    assert(wordSearch(board, 'cow') == False)
    assert(wordSearch(board, 'dab') == False)
    assert(wordSearch(board, 'goat') == False)
    assert(wordSearch(board, 'www') == False)

def main():
    testWordSearch()

main()
