from cmu_cpcs_utils import testFunction
import string

def areAnagrams(s1, s2):
    s1Low=s1.lower()
    s2Low=s2.lower()
    for c1 in s1Low:
        count1=s1Low.count(c1)
        count2=s2Low.count(c1)
        if count1!=count2:
            return False
    for c2 in s2Low:
        count3=s1Low.count(c2)
        count4=s2Low.count(c2)
        if count3!=count4:
            return False
    return True

@testFunction
def testAreAnagrams():
    assert(areAnagrams('Abca', 'BAAc') == True)
    assert(areAnagrams('Word', 'word') == True)
    assert(areAnagrams('CAT', 'act') == True)
    assert(areAnagrams('', '') == True)
    assert(areAnagrams('abcd', 'abc') == False)
    assert(areAnagrams('abc', 'abcd') == False)
    assert(areAnagrams('abc', 'abd') == False)
    assert(areAnagrams('abc', 'abc') == True)

def main():
    testAreAnagrams()

main()
