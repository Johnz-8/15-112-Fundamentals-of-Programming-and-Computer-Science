from cmu_cpcs_utils import testFunction

def firstNEvenFibonacciNumbers(n):
    result=[]
    FibonacciNumbers=[1,1]
    while len(result)<n:
        num=FibonacciNumbers[-1]+FibonacciNumbers[-2]
        FibonacciNumbers.append(num)
        if num%2==0:
            result.append(num)
    return result
        
@testFunction
def testFirstNEvenFibonacciNumbers():
    assert(firstNEvenFibonacciNumbers(0) == [])
    assert(firstNEvenFibonacciNumbers(1) == [2])
    assert(firstNEvenFibonacciNumbers(2) == [2, 8])
    assert(firstNEvenFibonacciNumbers(3) == [2, 8, 34])
    assert(firstNEvenFibonacciNumbers(4) == [2, 8, 34, 144])
    assert(firstNEvenFibonacciNumbers(5) == [2, 8, 34, 144, 610])

def main():
    testFirstNEvenFibonacciNumbers()

main()
