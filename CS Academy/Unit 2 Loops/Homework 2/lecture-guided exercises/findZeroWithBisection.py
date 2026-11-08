from cmu_cpcs_utils import testFunction, almostEqual
def getSign(x):
    return 1 if x>=0 else -1

def findZeroWithBisection(f, x0, x1, epsilon):
    while (x1-x0)>epsilon:
        xMid=(x1+x0)/2
    
        if getSign(f(xMid))==getSign(f(x0)):
            x0=xMid
        else:
            x1=xMid
        
    return xMid

@testFunction
def testFindZeroWithBisection():
    def f0(x): return 1 - x
    x = findZeroWithBisection(f0, 0, 4, 0.000000001)
    assert(almostEqual(x, 1))

    def f1(x): return x + 2.6
    x = findZeroWithBisection(f1, -3, -2, 0.25)
    assert(almostEqual(x, -2.75))

    def f2(x): return x*x - 2                          # root at x=sqrt(2)
    x = findZeroWithBisection(f2, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.414213562))

    def f3(x): return x**2 - (x + 1)                   # root at x=phi
    x = findZeroWithBisection(f3, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.618033989))

    def f4(x): return x**5 - 2**x                      # f(1)<0, f(2)>0
    x = findZeroWithBisection(f4, 1, 2, 0.000000001)
    assert(almostEqual(x, 1.177278551))

    def f5(x): return (10**-10) * (x + 5)               # f(-7)<0, f(-4)>0
    x = findZeroWithBisection(f5, -7, -4, 0.000000001)
    assert(almostEqual(x, -5))


def main():
    testFindZeroWithBisection()
main()
