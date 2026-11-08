from cmu_cpcs_utils import testFunction

def hasBalancedParentheses(s):
    count=0
    for c in s:
        if c=='(':
            count+=1
        if c==')':
            if count==0:
                return False
            count-=1
    return count==0

@testFunction
def testHasBalancedParentheses():
    assert(hasBalancedParentheses('( ( ( ) ( ) ) ( ) )') == True)
    assert(hasBalancedParentheses('( ) )') == False)
    assert(hasBalancedParentheses('( ) ) (') == False)
    assert(hasBalancedParentheses('( ( ) ) (') == False)
    assert(hasBalancedParentheses('(hI!)(Whats up?)(not much)') == True)
    assert(hasBalancedParentheses('((((hEy!)hi!)))') == True)
    assert(hasBalancedParentheses('!!!!') == True)

def main():
    testHasBalancedParentheses()

main()
