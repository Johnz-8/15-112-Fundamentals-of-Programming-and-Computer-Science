from cmu_cpcs_utils import testFunction

class Duration:
    def __init__(self, hours, minutes):
        self.hours=hours
        if minutes>=60:
            self.hours+=minutes//60
            self.minutes=minutes%60
        else:
           self.minutes=minutes
    
    def __repr__(self):
        return f'{self.hours}h:{self.minutes}m'
    
    def __eq__(self, other):
        return (isinstance(other, Duration) and
                self.hours==other.hours and 
                self.minutes==other.minutes)
    
    def __hash__(self):
        return hash(str(self))
    
    def add(self, other):
        if isinstance(other, Duration):
            return Duration((self.hours+other.hours), (self.minutes+other.minutes))

@testFunction
def testDurationClass():
    # A duration of 3 hours and 20 minutes
    d1 = Duration(3, 20) 
    assert(d1.hours == 3)
    assert(d1.minutes == 20)
    assert(str(d1) == '3h:20m') 

    # When an instance is created, if it has 60 or more minutes, 
    # convert them into hours as appropriate, always leaving 
    # fewer than 60 minutes. Assume minutes are always non-negative.
    d2 = Duration(4, 150)
    # Since 150m = 2h30m, the duration is 6h30m.
    assert(str(d2) == '6h:30m')

    L = [d1, d2]
    assert(str(L) == '[3h:20m, 6h:30m]')

    assert(d1 == Duration(3, 20))
    assert(d1 != Duration(4, 20))
    assert(d1 != Duration(3, 40))
    assert(d1 != 'do not crash here')

    s = set()
    assert(Duration(5, 18) not in s)
    s.add(Duration(5, 18))
    assert(Duration(5, 18) in s)

    # Adding two instances creates a new instance
    # with combined hours and minutes.
    d3 = Duration(2, 45)
    d4 = Duration(3, 30)
    d5 = d3.add(d4)
    assert(str(d5) == '6h:15m')
    
    # Do not create a new instance if the add 
    # method is given an invalid parameter
    dBad = 'do not crash on the next line!'
    d3.add(dBad)

def main():
    testDurationClass()

main()
