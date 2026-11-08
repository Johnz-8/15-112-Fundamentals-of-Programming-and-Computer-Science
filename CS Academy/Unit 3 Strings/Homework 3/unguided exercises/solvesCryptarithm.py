from cmu_cpcs_utils import testFunction
def setDigitToChr(string,Chr,digit):
    result=''
    for c in string:
        if c==Chr:
            result+=str(digit)
        else:
            result+=c
    return result

def containsLetter(str):
    for c in str:
        if c.isalpha():
            return True
    return False

def solvesCryptarithm(puzzle, solution):
    plusSignIdx=puzzle.find(' + ')
    equalSignIdx=puzzle.find(' = ')
    str1=puzzle[:plusSignIdx]
    str2=puzzle[plusSignIdx+3:equalSignIdx]
    strResult=puzzle[equalSignIdx+3:]
    for i in range(len(solution)):
        if '-' in solution[i]:
            continue
        Chr=solution[i]
        str1=setDigitToChr(str1,Chr,i)
        str2=setDigitToChr(str2,Chr,i)
        strResult=setDigitToChr(strResult,Chr,i)
    
    if containsLetter(str1) or containsLetter(str2) or containsLetter(strResult):
        return False
    return int(str1)+int(str2)==int(strResult)

@testFunction
def testSolvesCryptarithm():
    #                         9567 + 1085 = 10652
    assert(solvesCryptarithm('SEND + MORE = MONEY', 'OMY--ENDRS') == True)

    #                         201689 + 201689 = 403378
    assert(solvesCryptarithm('NUMBER + NUMBER = PUZZLE', 'UMNZP-BLER') == True)

    #                         91542 + 3077542 = 3169084
    assert(solvesCryptarithm('TILES + PUZZLES = PICTURE', 'UISPELCZRT') == True)

    #                         8456 + 1074 = 10542 (False)
    assert(solvesCryptarithm('SEND + MORE = MONEY', 'OMY-ENDRS') == False)

    #                         9567 + 1085 = 1062 (False)
    assert(solvesCryptarithm('SEND + MORE = MONY', 'OMY--ENDRS') == False)

    #                         No S in solution
    assert(solvesCryptarithm('SEND + MORE = MONEY', 'OMY--ENDR-') == False)

def main():
    testSolvesCryptarithm()
main()
