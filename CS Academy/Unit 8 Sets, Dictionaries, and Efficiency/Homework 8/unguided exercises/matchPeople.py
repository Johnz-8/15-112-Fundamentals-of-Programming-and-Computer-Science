from cmu_cpcs_utils import testFunction
import copy

def matchPeople(people, traits):
    res=dict()
    res['close matches']=set()
    res['loose matches']=set()
    res['no matches']=set()
    for name in people:
        count=0
        setOfTraits=people[name]
        for trait in traits:
            if trait in setOfTraits:
                count+=1
        if count==3 or count==4:
            res['close matches'].add(name)
        elif count==1 or count==2:
            res['loose matches'].add(name)
        else:
            res['no matches'].add(name)
    return res

@testFunction
def testMatchPeople():
    people = {
        'Amy': {'Creative', 'Ambitious', 'Conscientious', 'Flexible'},
        'Ben': {'Conscientious', 'Ambitious', 'Persistent', 'Honest'},
        'Claire': {'Creative', 'Loyal', 'Ambitious', 'Persistent'},
        'Dale': {'Courageous', 'Ambitious', 'Honest', 'Honorable'},
        'Evan': {'Flexible', 'Patient', 'Disciplined', 'Honorable'},
        'Fred': {'Courageous', 'Curious', 'Resilient', 'Compassionate'},
        'Grace': {'Conscientious', 'Curious', 'Honorable', 'Compassionate'}
    }
    people1 = copy.deepcopy(people) # Used to verify function is nonmutating

    traits1 = {'Creative', 'Honest', 'Ambitious', 'Persistent'}
    assert(matchPeople(people, traits1) == {
           'close matches': {'Ben', 'Claire'},
           'loose matches': {'Dale', 'Amy'},
           'no matches': {'Fred', 'Grace', 'Evan'}
        })
    
    assert(people == people1) # Verify that the function is nonmutating

    traits2 = {'Courageous', 'Curious', 'Resilient', 'Compassionate'}
    assert(matchPeople(people, traits2) == {
           'close matches': {'Fred'},
           'loose matches': {'Dale', 'Grace'},
           'no matches': {'Claire', 'Amy', 'Evan', 'Ben'}
        })

    assert(matchPeople(dict(), traits2) == {
           'close matches': set(),
           'loose matches': set(),
           'no matches': set()
        })


def main():
    testMatchPeople()

main()
