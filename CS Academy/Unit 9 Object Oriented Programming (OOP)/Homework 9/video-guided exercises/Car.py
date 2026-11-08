from cmu_cpcs_utils import testFunction

class Car:
    def __init__(self, make, model, mpg, tankSize, price):
        self.make=make
        self.model=model
        self.mpg=mpg
        self.tankSize=tankSize
        self.price=price
    def getRange(self):
        return self.mpg*self.tankSize
    def getUsedPrice(self, years):
        assert(years>0)
        rate=0.8-(years-1)*0.1
        if rate<0.2:
            rate=0.2
        return int(rate*self.price)

@testFunction
def testCarClass():
    car1 = Car('Ford', 'Mustang', 30, 15, 32000)
    assert(car1.make == 'Ford')
    assert(car1.model == 'Mustang')
    assert(car1.mpg == 30) # miles per gallon
    assert(car1.tankSize == 15) # gallons in a full tank
    assert(car1.getRange() == 450) # max miles on a full tank

    # Assume that a car loses 20% of its value in the first year, then 10% more
    # each following year, but never falls below 20% of its original value.
    # Hint: use int() to convert result to an integer.
    assert(car1.price == 32000) # in dollars
    assert(car1.getUsedPrice(1) == 25600) # after 1 year, $25,600 (80% of $32,000)
    assert(car1.getUsedPrice(2) == 22400) # after 2 years, $22,400 (70% of $32,000)
    assert(car1.getUsedPrice(7) ==  6400) # after 7 years, $6,400 (20% of $32,000)
    assert(car1.getUsedPrice(8) ==  6400) # does not fall below 20% of original value

    car2 = Car('Toyota', 'Prius', 57, 11, 28000)
    assert(car2.make == 'Toyota')
    assert(car2.model == 'Prius')
    assert(car2.mpg == 57)
    assert(car2.tankSize == 11)
    assert(car2.getRange() == 627)

    assert(car2.price == 28000)
    assert(car2.getUsedPrice(1) == 22400) # after 1 year, $22,400 (80% of $28,000)
    assert(car2.getUsedPrice(2) == 19600) # after 2 years, $19,600 (70% of $28,000)
    assert(car2.getUsedPrice(7) ==  5600) # after 7 years, $5,600 (20% of $28,000)
    assert(car2.getUsedPrice(8) ==  5600) # does not fall below 20% of original value

def main():
    testCarClass()

main()
