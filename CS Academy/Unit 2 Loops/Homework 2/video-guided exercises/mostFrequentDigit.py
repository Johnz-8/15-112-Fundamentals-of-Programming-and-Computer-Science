from cmu_cpcs_utils import testFunction

def digitOccurences(n,digit):
    if (n==0 and digit==0):
        return 1
    count=0
    while n>0:
        currentDigit=n%10
        if currentDigit==digit:
            count+=1
        n//=10
    return count
    
def mostFrequentDigit(n):
    bestN=-1
    bestCount=-1
    n=abs(n)
    for digit in range(10):
        if digitOccurences(n,digit)>=bestCount:
            bestCount=digitOccurences(n,digit)
            bestN=digit
    
    return bestN 

@testFunction
def testMostFrequentDigit():
    assert(mostFrequentDigit(55) == 5)
    assert(mostFrequentDigit(1223) == 2)
    assert(mostFrequentDigit(33221) == 3)
    assert(mostFrequentDigit(23232) == 2)
    assert(mostFrequentDigit(12345) == 5)
    assert(mostFrequentDigit(0) == 0)
    assert(mostFrequentDigit(-12233) == 3)
    assert(mostFrequentDigit(-12345) == 5)

def main():
    testMostFrequentDigit()

main()
