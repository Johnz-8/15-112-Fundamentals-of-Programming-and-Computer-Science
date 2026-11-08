from cmu_cpcs_utils import testFunction
def consecutiveRun(n,digit):
    if n==digit==0:
        return 1
    currentRun=0
    MaxRun=0
    while n>0:
        currentDigit=n%10
        if currentDigit==digit:
            currentRun+=1
            MaxRun=max(currentRun,MaxRun)
        else:
            currentRun=0
        n//=10
    return MaxRun
    

def longestDigitRun(n):
    n=abs(n)
    longestDigit=-1
    longestCount=0
    for digit in range(10):
        count=consecutiveRun(n,digit)
        if count>=longestCount:
            longestDigit=digit
            longestCount=count
    return longestDigit

@testFunction
def testLongestDigitRun():
    assert(longestDigitRun(1177732) == 7)
    assert(longestDigitRun(6775566) == 7)
    assert(longestDigitRun(123) == 3)
    assert(longestDigitRun(229) == 2)
    assert(longestDigitRun(111) == 1)
    assert(longestDigitRun(0) == 0)
    assert(longestDigitRun(-6775566) == 7)

def main():
    testLongestDigitRun()

main()
