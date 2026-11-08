from cmu_cpcs_utils import testFunction

class Angle:
    def __init__(self, degrees):
        self.degrees=(degrees%360)
    
    def __repr__(self):
        return f'<{self.degrees} degree Angle>'

    def __eq__(self, other):
        return (isinstance(other,Angle) and
                self.degrees==other.degrees)
    
    def __hash__(self):
        return hash(self.degrees)

    def add(self, addend):
        if isinstance(addend, Angle):
            self.degrees+=addend.degrees
        else:
            self.degrees+=addend

    def bisect(self, other):
        return Angle(self.degrees+other.degrees//2)

@testFunction
def testAngleClass():
    angle1 = Angle(50)
    assert(angle1.degrees == 50)
    assert(str(angle1) == '<50 degree Angle>')

    angle2 = Angle(90)
    assert(angle2.degrees == 90)
    assert(str(angle2) == '<90 degree Angle>')

    L = [angle1, angle2]
    assert(str(L) == '[<50 degree Angle>, <90 degree Angle>]')

    angle1.add(30)
    assert(str(angle1) == '<80 degree Angle>')

    # Note that the add method works with either integers or Angles
    angle1.add(angle2)
    assert(str(angle1) == '<170 degree Angle>')

    # Angles are always non-negative and less than 360.
    # Hint: use the % operator to make this work right.
    angle3 = Angle(370)
    assert(angle3.degrees == 10)
    assert(str(angle3) == '<10 degree Angle>')

    angle4 = Angle(36030)
    assert(angle4.degrees == 30)
    assert(str(angle4) == '<30 degree Angle>')

    # To bisect, add half of the second angle to the first
    # (using floor division).
    angle5 = angle3.bisect(angle4)
    assert(angle5.degrees == 25) # 10 + 30//2
    assert(str(angle5) == '<25 degree Angle>')

    # equality:
    assert(angle5 == Angle(25))
    assert(angle5 != Angle(90))
    assert(angle5 != 'do not crash here')

    # hashing:
    s = set()
    assert(Angle(25) not in s)
    s.add(Angle(25))
    assert(Angle(25) in s)

def main():
    testAngleClass()

main()
