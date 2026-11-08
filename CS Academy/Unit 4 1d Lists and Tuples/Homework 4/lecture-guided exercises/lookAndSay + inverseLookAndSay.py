from cmu_cpcs_utils import testFunction

def lookAndSay(L):
    if L==[]:
        return []
    result=[]
    runNum=L[0]
    runCount=0
    for v in L:
        if v==runNum:
            runCount+=1
        else:
            result.append((runCount,runNum))
            runCount=1
            runNum=v
    result.append((runCount,runNum))
    return result

def inverseLookAndSay(L):
    result=[]
    for count,num in L:
        result.extend([num]*count)
    return result

@testFunction
def testLookAndSay():
    assert(lookAndSay([3, 3, 8, -10, -10, -10, 3]) ==
                      [(2, 3), (1, 8), (3, -10), (1, 3)])
    assert(lookAndSay([1, 1, 0, 0, 1, 1, 1]) == [(2, 1), (2, 0), (3, 1)])
    assert(lookAndSay([-5, 5]) == [(1, -5), (1, 5)])
    assert(lookAndSay([6]) == [(1, 6)])
    assert(lookAndSay([]) == [])

    # Verify that the function is non-mutating
    L = [3, 3, 8, -10, -10, -10, 3]
    lookAndSay(L)
    assert(L == [3, 3, 8, -10, -10, -10, 3])

@testFunction
def testInverseLookAndSay():
    assert(inverseLookAndSay([(2, 3), (1, 8), (3, -10), (1, 3)]) ==
                             [3, 3, 8, -10, -10, -10, 3])
    assert(inverseLookAndSay([(2, 1), (2, 0), (3, 1)]) == [1, 1, 0, 0, 1, 1, 1])
    assert(inverseLookAndSay([(1, -5), (1, 5)]) == [-5, 5])
    assert(inverseLookAndSay([(1, 6)]) == [6])
    assert(inverseLookAndSay([]) == [])

    # Verify that the function is non-mutating
    L = [(2, 3), (1, 8), (3, -10), (1, 3)]
    inverseLookAndSay(L)
    assert(L == [(2, 3), (1, 8), (3, -10), (1, 3)])

def main():
    testLookAndSay()
    testInverseLookAndSay()

main()
