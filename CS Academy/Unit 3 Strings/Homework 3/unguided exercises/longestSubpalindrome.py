from cmu_cpcs_utils import testFunction
def palindromeLength(s,leftIdx,rightIdx):
    left=s[:leftIdx+1]
    right=s[rightIdx:]
    invLeft=left[::-1]
    length=0
    for i in range(min(len(invLeft),len(right))):
        if invLeft[i]==right[i]:
            length+=1
        else:
            break
    return length

def longestSubpalindrome(s):
    longestPalindrome=''
    longestLength=0
    for i in range(len(s)):
        sideLength=palindromeLength(s,i-1,i+1)
        currLength=sideLength*2+1
        currPalindrome=s[i-sideLength:i+sideLength+1]
        if currLength>longestLength:
            longestLength=currLength
            longestPalindrome=currPalindrome
        elif currLength==longestLength:
            longestPalindrome=currPalindrome if currPalindrome>longestPalindrome else longestPalindrome
        #this is for even palindromes
        if i+1<len(s):
            sideLength=palindromeLength(s,i,i+1)
            currLength=sideLength*2
            currPalindrome=s[i-sideLength+1:i+sideLength+1]
            if currLength>longestLength:
                longestLength=currLength
                longestPalindrome=currPalindrome 
            elif currLength==longestLength:
                longestPalindrome=currPalindrome if currPalindrome>longestPalindrome else longestPalindrome
    return longestPalindrome

@testFunction
def testLongestSubpalindrome():
    assert(longestSubpalindrome('ab-4-be!!!') == 'b-4-b')
    assert(longestSubpalindrome('abcbce') == 'cbc')
    assert(longestSubpalindrome('aba') == 'aba')
    assert(longestSubpalindrome('a') == 'a')
    assert(longestSubpalindrome('abd') == 'd')
    assert(longestSubpalindrome('kP:p') == 'p')
    assert(longestSubpalindrome('') == '')
def main():
    testLongestSubpalindrome()
main()