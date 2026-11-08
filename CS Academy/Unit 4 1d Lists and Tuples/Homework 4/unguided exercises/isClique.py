from cmu_cpcs_utils import testFunction
import copy

def getAllPeople(friends):
    result=[]
    for term in friends:
        for name in term:
            if result.count(name)==0:
                result.append(name)
    return result

def isClique(friends):
    names=getAllPeople(friends)
    allPossiblePairs=[]
    for i in range(len(names)):
        for j in range(i,len(names)):
            if names[i] != names[j]:
                allPossiblePairs.append((names[i], names[j])) 

    for pair in allPossiblePairs:
        if friends.count(pair)>0 or friends.count(pair[::-1])>0:
            continue
        else:
            return False
    return True

@testFunction
def testIsClique():
    assert(isClique([ ('Fred', 'Wilma'),
                      ('Barney', 'Fred'),
                      ('Wilma', 'Barney') ]) == True)

    assert(isClique([ ('Fred', 'Wilma'),
                      ('Barney', 'Fred'),
                      ('Wilma', 'Barney'),
                      ('Betty', 'Barney'),
                      ('Wilma', 'Betty') ]) == False)

    assert(isClique([ ('Fred', 'Wilma') ]) == True)

    assert(isClique([ ('Fred', 'Wilma'),
                      ('Betty', 'Barney') ]) == False)

def main():
    testIsClique()
main()
