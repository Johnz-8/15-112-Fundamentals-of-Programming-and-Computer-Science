from cmu_cpcs_utils import testFunction

def getAscend(n):
    ones=n%10
    tens=n//10%10
    hundreds=n//100
    smallestDigit=min(ones,tens,hundreds)
    biggestDigit=max(ones,tens,hundreds)
    return smallestDigit*100+(ones+tens+hundreds-biggestDigit-smallestDigit)*10+biggestDigit
def getDescend(n):
    ones=n%10
    tens=n//10%10
    hundreds=n//100
    smallestDigit=min(ones,tens,hundreds)
    biggestDigit=max(ones,tens,hundreds)
    return biggestDigit*100+(ones+tens+hundreds-biggestDigit-smallestDigit)*10+smallestDigit
def stepsToReach495(n):
    if n%111==0:
        return None
    nAscend=getAscend(n)
    nDescend=getDescend(n)
    count=0
    while n!=495:
        n=getDescend(n)-getAscend(n)
        count+=1
    return count

@testFunction
def testStepsToReach495():
    assert(stepsToReach495(495) == 0)

    assert(stepsToReach495(594) == 1) # 954 - 459 = 495

    assert(stepsToReach495(396) == 2) # 963 - 369 = 594
                                      # 954 - 459 = 495

    assert(stepsToReach495(936) == 2) # Same as 396

    assert(stepsToReach495(251) == 3) # 521 - 125 = 396
                                      # 963 - 369 = 594
                                      # 954 - 459 = 495
    
    assert(stepsToReach495(516) == 1) # 651 - 156 = 495

    assert(stepsToReach495(891) == 4)

    assert(stepsToReach495(898) == 6) # 988 - 889 = 099
                                      # 990 - 099 = 891
                                      # 981 - 189 = 792
                                      # 972 - 279 = 693
                                      # 963 - 369 = 594
                                      # 954 - 459 = 495

    assert(stepsToReach495(111) == None)
    assert(stepsToReach495(555) == None)
    assert(stepsToReach495(777) == None)

def main():
    testStepsToReach495()

main()
