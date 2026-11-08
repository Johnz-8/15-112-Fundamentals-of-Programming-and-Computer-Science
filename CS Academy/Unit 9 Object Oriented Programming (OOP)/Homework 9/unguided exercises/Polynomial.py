from cmu_cpcs_utils import testFunction
import copy

class Polynomial:
    def __init__(self, coeffs):
        self.coeffs=coeffs
    
    def __repr__(self):
        return coefficientsToString(self.coeffs)
    
    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.coeffs==other.coeffs
        elif isinstance(other, list):
            return self.coeffs==other
        else:
            return False
    
    def __hash__(self):
        return hash(tuple(self.coeffs))
        
    def evalAt(self, x):
        result=0
        for i in range(len(self.coeffs)-1, -1, -1):
            order=len(self.coeffs)-(i+1)
            result+=self.coeffs[i]*x**order
        return result
    
    def plus(self, other):
        revSelf=self.coeffs[::-1]
        revOther=other.coeffs[::-1]
        revRes=[]
        if len(revSelf)>len(revOther):
            for i in range(len(revOther)):
                revRes.append(revSelf[i]+revOther[i])
            revRes+=revSelf[len(revOther):]
        else:
            for i in range(len(revSelf)):
                revRes.append(revSelf[i]+revOther[i])
            revRes+=revOther[len(revSelf):]
        
        return Polynomial(revRes[::-1])
            

def coefficientsToString(coeffs):
    # This helper function may be useful for your __repr__ method!
    if len(coeffs) == 1:
        return str(coeffs[0])
    else:
        terms = [ ]
        for i in range(len(coeffs)):
            coeff = coeffs[i]
            if (coeff != 0):
                isNegative = (coeff < 0)
                coeff = abs(coeff)
                if (terms != [ ]):
                    terms.append(' - ' if isNegative else ' + ')
                if (terms == [ ]) and isNegative:
                    terms.append('-')
                if ((coeff != 1) or (i == len(coeffs)-1)):
                    terms.append(str(coeff))
                power = len(coeffs)-1-i
                if (power == 1): terms.append('x')
                elif (power > 1): terms.append(f'x**{power}')
        return ''.join(terms)

@testFunction
def testPolynomialClass():
    p1 = Polynomial([2, 3]) # 2x + 3
    # Write __init__, and store the coefficients in the coeffs property:
    assert(p1.coeffs == [2, 3])

    # Write __repr__, and remember to use coefficientsToString(coeffs):
    assert(str(p1) == '2x + 3')

    # Write evalAt, which evaluates this polynomial at the given x value:
    assert(p1.evalAt(5) == 13)

    p2 = Polynomial([3, 0, -1]) # 3x**2 - 1
    assert(p2.coeffs == [3, 0, -1])
    assert(str(p2) == '3x**2 - 1')
    assert(p2.evalAt(5) == 74)

    L = [p1, p2]
    assert(str(L) == '[2x + 3, 3x**2 - 1]')

    # Write plus, which takes a second Polynomial instance, and returns a
    # third Polynomial, which is the sum of the two polynomials.
    # To add two polynomials, just add the like terms:
    p3 = p1.plus(p2) # (2x + 3) + (3x**2 - 1) == 3x**2 + 2x + 2

    assert(p3.coeffs == [3, 2, 2])
    assert(str(p3) == '3x**2 + 2x + 2')
    assert(p3.evalAt(10) == 322)

    p4 = p2.plus(p1) # (3x**2 - 1) + (2x + 3) == 3x**2 + 2x + 2
    assert(p4.coeffs == [3, 2, 2])
    assert(str(p4) == '3x**2 + 2x + 2')
    assert(p4.evalAt(10) == 322)

    # Write __eq__ properly:
    assert(p3 != p1)
    assert(p3 == p4)
    assert(p3 != 'ack') # do not crash here!

    # And write __hash__ properly:
    s = set()
    assert(p3 not in s)
    s.add(p3)
    assert(p3 in s)
    assert(p4 in s)

def main():
    testPolynomialClass()

main()
