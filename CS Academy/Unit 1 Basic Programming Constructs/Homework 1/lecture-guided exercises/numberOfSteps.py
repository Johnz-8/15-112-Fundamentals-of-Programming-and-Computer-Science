from cmu_cpcs_utils import testFunction
import math

def numberOfSteps(bricks):
    return math.ceil((-1+(1+8*bricks)**0.5)/2)

@testFunction
def testNumberOfSteps():
    assert(numberOfSteps(0) == 0)
    assert(numberOfSteps(1) == 1)
    assert(numberOfSteps(2) == 2)
    assert(numberOfSteps(3) == 2)
    assert(numberOfSteps(4) == 3)
    assert(numberOfSteps(6) == 3)
    assert(numberOfSteps(7) == 4)
    assert(numberOfSteps(10) == 4)
    assert(numberOfSteps(11) == 5)
    assert(numberOfSteps(55) == 10)
    assert(numberOfSteps(56) == 11)

def main():
    testNumberOfSteps()

main()