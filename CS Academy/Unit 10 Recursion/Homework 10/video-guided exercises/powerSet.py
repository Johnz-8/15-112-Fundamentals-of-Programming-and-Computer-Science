from cmu_cpcs_utils import testFunction

def powerSet(L):
    if L==[]:
        return [[]]
    else:
        first=L[0]
        rest=L[1:]
        allSublists=[]
        for sublist in powerSet(rest):
            allSublists.append(sublist)
            allSublists.append([first]+sublist)
        return sorted(allSublists)

@testFunction
def testPowerSet():
    # Make sure that your output list is sorted. 
    L = [1, 2, 3]
    output = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert(powerSet(L) == sorted(output))

    L = [5, -8]
    output = [[], [-8], [5], [5, -8]]
    assert(powerSet(L) == sorted(output))

    L = [-1]
    output = [[], [-1]]
    assert(powerSet(L) == sorted(output))

    L = []
    assert(powerSet(L) == [[]])

def main():
    testPowerSet()

main()
