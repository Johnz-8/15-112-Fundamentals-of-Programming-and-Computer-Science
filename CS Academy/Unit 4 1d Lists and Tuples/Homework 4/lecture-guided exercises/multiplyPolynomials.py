from cmu_cpcs_utils import testFunction

def multiplyPolynomials(p1, p2):
    result=[0]*(len(p1)+len(p2)-1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i+j]+=p1[i]*p2[j]
    return result

@testFunction
def testMultiplyPolynomials():
    assert(multiplyPolynomials([2, 3, 0, 4], [1, 5]) == [2, 13, 15, 4, 20])
    assert(multiplyPolynomials([1, 5], [2, 3, 0, 4]) == [2, 13, 15, 4, 20])
    assert(multiplyPolynomials([7, 3], [2, 4]) == [14, 34, 12])
    assert(multiplyPolynomials([-2, -1], [-2, 4]) == [4, -6, -4])
    assert(multiplyPolynomials([3], [5]) == [15])
    assert(multiplyPolynomials([0], [2, 1]) == [0, 0])

    #  Finally, verify that the function is non-mutating:
    p1 = [2, 3]
    p2 = [4, 5, 6]
    multiplyPolynomials(p1, p2)
    assert(p1, p2 == p1, p2)

def main():
    testMultiplyPolynomials()

main()
