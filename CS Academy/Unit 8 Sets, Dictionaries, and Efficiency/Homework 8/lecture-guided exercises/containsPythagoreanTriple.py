from cmu_cpcs_utils import testFunction, rounded

def containsPythagoreanTriple(L):
    s=set(L)
    for i in range(len(L)-1):
        a=L[i]
        for j in range(i+1,len(L)):
            b=L[j]
            c=rounded((a**2+b**2)**0.5)
            if (a**2+b**2==c**2) and (c in s):
                return True
    return False

@testFunction
def testContainsPythagoreanTriple():
    # 3, 4, 5 is a Pythagorean Triple
    assert(containsPythagoreanTriple([1, 3, 6, 5, 1, 4]) == True)
    # 5, 12, 13 is a Pythagorean Triple
    assert(containsPythagoreanTriple([5, 7, 1, 6, 12, 13]) == True)
    # 6, 8, 10 is a Pythagorean Triple
    assert(containsPythagoreanTriple([8, 6, 10]) == True)
    # 8, 15, 17 is a Pythagorean Triple
    assert(containsPythagoreanTriple([2, 8, 15, 16, 17]) == True)

    assert(containsPythagoreanTriple([1, 3, 6, 2, 8, 1, 4]) == False)
    assert(containsPythagoreanTriple([21, 3, 2, 7, 5]) == False)
    assert(containsPythagoreanTriple([5, 13]) == False)
    assert(containsPythagoreanTriple([]) == False)

def main():
    testContainsPythagoreanTriple()

main()
