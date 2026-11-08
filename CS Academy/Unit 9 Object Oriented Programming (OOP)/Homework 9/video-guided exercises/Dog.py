from cmu_cpcs_utils import testFunction

class Dog:
    def __init__(self, name, breed, age):
        self.name=name
        self.breed=breed
        self.age=age
    def getHumanAge(self):
        return self.age*7
    def isPuppy(self):
        return self.age<=1

@testFunction
def testDogClass():
    dog1 = Dog('Spot', 'Poodle', 3)
    assert(dog1.name == 'Spot')
    assert(dog1.breed == 'Poodle')
    assert(dog1.age == 3) # years
    assert(dog1.getHumanAge() == 21) # years (7 * dog age)
    assert(dog1.isPuppy() == False)  # puppies are <= 1 year old

    dog2 = Dog('Bella', 'Beagle', 1)
    assert(dog2.name == 'Bella')
    assert(dog2.breed == 'Beagle')
    assert(dog2.age == 1) # years
    assert(dog2.getHumanAge() == 7) # years (7 * dog age)
    assert(dog2.isPuppy() == True)  # puppies are <= 1 year old

def main():
    testDogClass()

main()
