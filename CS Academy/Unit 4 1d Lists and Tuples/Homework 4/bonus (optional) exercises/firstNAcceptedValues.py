from cmu_cpcs_utils import testFunction
import copy

def isAcceptedValue(x, rules):
    mustBe=True
    equalTo=0
    multipleOf=0
    for term in rules:
        L=term.split(' ')
        value=L[0]
        modulo=int(value[2:]) if value[2:] != '' else x+1 #to canonicalize input to x%modulo
        if L[2]=='not':
            mustBe=False
        else:
            mustBe=True
        
        if L.count('equal')==1:
            equalTo=int(L[-1])
            if mustBe:
                if x%modulo!=equalTo:
                    return False
            else:
                if x%modulo==equalTo:
                    return False
        else:
            multipleOf=int(L[-1])
            if mustBe:
                if x%modulo%multipleOf!=0:
                    return False
            else:
                if x%modulo%multipleOf==0:
                    return False
    return True

def firstNAcceptedValues(n, rules):
    result=[]
    count=0
    currNum=1
    while count<n:
        if isAcceptedValue(currNum,rules):
            result.append(currNum)
            count+=1
        currNum+=1
    return result

@testFunction
def testIsAcceptedValue():
    rules = ['x must be a multiple of 3']
    assert(isAcceptedValue(3, rules) == True)
    assert(isAcceptedValue(5, rules) == False)

    rules = ['x must be equal to 9']
    assert(isAcceptedValue(3, rules) == False)
    assert(isAcceptedValue(9, rules) == True)
    
    rules = ['x must not be a multiple of 9']
    assert(isAcceptedValue(5, rules) == True)
    assert(isAcceptedValue(9, rules) == False)
    
    rules = ['x%10 must not be equal to 4']
    assert(isAcceptedValue(14, rules) == False)
    assert(isAcceptedValue(18, rules) == True)

    rules = ['x must be a multiple of 3',
              'x must not be a multiple of 9']
    assert(isAcceptedValue(3, rules) == True)
    assert(isAcceptedValue(15, rules) == True)
    assert(isAcceptedValue(20, rules) == False)

    rules = ['x must not be equal to 5',
             'x%10 must not be a multiple of 3']
    assert(isAcceptedValue(4, rules) == True)
    assert(isAcceptedValue(5, rules) == False)
    assert(isAcceptedValue(9, rules) == False)
    
    rules = ['x must be a multiple of 3',
             'x must not be a multiple of 9',
             'x%2 must be a multiple of 2',
             'x%10 must not be equal to 4']
    assert(isAcceptedValue(6, rules) == True)
    assert(isAcceptedValue(40, rules) == False)
    assert(isAcceptedValue(48, rules) == True)

@testFunction
def testFirstNAcceptedValues():
    rules = ['x must be a multiple of 3']
    assert(firstNAcceptedValues(0, rules) == [])
    assert(firstNAcceptedValues(3, rules) == [3, 6, 9])
    assert(firstNAcceptedValues(6, rules) == [3, 6, 9, 12, 15, 18])

    rules = ['x must be a multiple of 3',
             'x must not be a multiple of 9']
    assert(firstNAcceptedValues(6, rules) == [3, 6, 12, 15, 21, 24])

    rules = ['x must be a multiple of 3',
             'x must not be a multiple of 9',
             'x%2 must be a multiple of 2',
             'x%10 must not be equal to 4']
    assert(firstNAcceptedValues(6, rules) == [6, 12, 30, 42, 48, 60])

    rules = ['x%2 must be equal to 1',
             'x%5 must not be a multiple of 2',
             'x must not be equal to 3']
    assert(firstNAcceptedValues(6, rules) == [1, 11, 13, 21, 23, 31])

    # Verify that the function is non-mutating
    rules = ['x must be a multiple of 3']
    firstNAcceptedValues(6, rules)
    assert(rules == ['x must be a multiple of 3'] )

def main():
    testIsAcceptedValue()
    testFirstNAcceptedValues()

main()
