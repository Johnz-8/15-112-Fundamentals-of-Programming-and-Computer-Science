from cmu_cpcs_utils import testFunction, almostEqual

def nthFibonacciNumber(n):
    n+=1
    return ((1+5**0.5)**n-(1-5**0.5)**n)/(2**n*5**0.5)

@testFunction
def testNthFibonacciNumber():
    assert(almostEqual(nthFibonacciNumber(0), 1))
    assert(almostEqual(nthFibonacciNumber(1), 1))
    assert(almostEqual(nthFibonacciNumber(2), 2))
    assert(almostEqual(nthFibonacciNumber(3), 3))
    assert(almostEqual(nthFibonacciNumber(4), 5))
    assert(almostEqual(nthFibonacciNumber(5), 8))


def main():
    testNthFibonacciNumber()

main()
