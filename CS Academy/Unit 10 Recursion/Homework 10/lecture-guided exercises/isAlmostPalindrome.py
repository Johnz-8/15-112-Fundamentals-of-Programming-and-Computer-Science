from cmu_cpcs_utils import testFunction

def isAlmostPalindrome(s):
    if countDifference(s)==1:
        return True
    else:
        return False
    
def countDifference(s):
    if len(s)==1 or len(s)==0:
        return 0
    else:
        first, last=s[0], s[-1]
        rest=s[1:-1]
        if first==last:
            return countDifference(rest)
        else:
            return 1+countDifference(rest)

@testFunction
def testIsAlmostPalindrome():
    assert(isAlmostPalindrome('stars') == True)  # r -> t
    assert(isAlmostPalindrome('abca') == True)   # c -> b
    assert(isAlmostPalindrome('abc') == True)    # c -> a
    assert(isAlmostPalindrome('abcb') == False) 
    assert(isAlmostPalindrome('kayak') == False) # already a palindrome!
    assert(isAlmostPalindrome('a') == False)     # already a palindrome!
    assert(isAlmostPalindrome('') == False)      # already a palindrome!

def main():
    testIsAlmostPalindrome()

main()
