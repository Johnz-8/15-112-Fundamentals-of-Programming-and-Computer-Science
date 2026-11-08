from cmu_cpcs_utils import testFunction
def wordSearch(board, word):
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == word[0]:
                result = findWordFromCell(board, word, row, col)
                if result != None:
                    return f'{repr(word)} is at {row, col} heading {result}'
    return f'{repr(word)} not found'

def findWordFromCell(board, word, row, col):
    rows, cols = len(board), len(board[0])
    drows = [-1, 0, 1]
    dcols = [-1, 0, 1]
    for drow in drows:
        for dcol in dcols:
            if drow==dcol==0:
                continue
            result=findWordFromDirection(board, word, row, col, drow, dcol)
            if result!=None:
                return result
    return None

def findWordFromDirection(board, word, row, col, drow, dcol):
    rows, cols = len(board), len(board[0])
    for i in range(len(word)):
        newRow=row+drow*i
        newCol=col+dcol*i
        if (newRow>=rows or
        newRow<0 or
        newCol>=cols or
        newCol<0 or
        board[newRow][newCol]!=word[i]):
            return None
    return getDirection(drow+1,dcol+1)
 
def getDirection(drow, dcol):
    dirNames = [ [ 'up-left'  ,  'up' , 'up-right'   ],
             [ 'left'     ,   ''  , 'right'      ],
             [ 'down-left', 'down', 'down-right' ] ]
    return dirNames[drow][dcol]

@testFunction
def testWordSearch():
    board = [ [ 'd', 'o', 'g' ],
              [ 't', 'a', 'c' ],
              [ 'w', 'a', 't' ],
              [ 'u', 'r', 'b' ] ]
    assert(wordSearch(board, 'dog') == "'dog' is at (0, 0) heading right")
    assert(wordSearch(board, 'cat') == "'cat' is at (1, 2) heading left")
    assert(wordSearch(board, 'bat') == "'bat' is at (3, 2) heading up-left")
    assert(wordSearch(board, 'tab') == "'tab' is at (1, 0) heading down-right")
    assert(wordSearch(board, 'wag') == "'wag' is at (2, 0) heading up-right")
    assert(wordSearch(board, 'cow') == "'cow' not found")
    assert(wordSearch(board, 'dab') == "'dab' not found")
    assert(wordSearch(board, 'goat') == "'goat' not found")
    assert(wordSearch(board, 'www') == "'www' not found")

def main():
    testWordSearch()

main()
