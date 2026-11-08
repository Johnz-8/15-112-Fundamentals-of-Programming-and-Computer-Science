from cmu_cpcs_utils import testFunction

def evalPolynomial(p, x):
    result=0
    sign=1
    for term in p.split(' '):
        if term=="+":
            sign=1
        elif term=='-':
            sign=-1
        # term can be in the form '4' '4x' '4x^2' 'x^2', transform them into ax^b
        if term[0]=='x':
            term='1'+term
        if 'x' not in term:
            term=term+'x^0'
        if '^' not in term:
            term=term+'^1'
        
        xIndex=term.find('x')
        coefficient=int(term[:xIndex])
        order=int(term[xIndex+2:])
        result+=sign*coefficient*x**order
    return result

@testFunction
def testEvalPolynomial():
    assert(evalPolynomial('4', 2) == 4)
    assert(evalPolynomial('x', 6) == 6)
    assert(evalPolynomial('x^2 + 2x - 7', 3) == 8)
    assert(evalPolynomial('3x^2 + 4', 10) == 304)
    assert(evalPolynomial('5x^3 + 4x + 1', 1) == 10)
    assert(evalPolynomial('4x^3 + x', -2) == -34)
    assert(evalPolynomial('10x^3 + 12x + 4', 3) == 310)
    assert(evalPolynomial('-10x^3', 3) == -270)
    
def main():
    testEvalPolynomial()

main()
