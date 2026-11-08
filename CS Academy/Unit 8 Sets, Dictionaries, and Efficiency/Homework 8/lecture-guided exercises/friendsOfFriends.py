from cmu_cpcs_utils import testFunction
import copy

def friendsOfFriends(friends):
    fof=dict()
    for name in friends:
        fof[name]=set()
        for friend in friends[name]:
            for friendOfFriends in friends[friend]:
                if friendOfFriends!=name and (friendOfFriends not in friends[name]):
                    fof[name].add(friendOfFriends)
    return fof
            

@testFunction
def testFriendsOfFriends():
    friends = {
                'Fred'   : {'Wilma', 'Betty', 'Robert'},
                'Betty'  : {'Alice', 'Wilma'},
                'Wilma'  : {'Fred'},
                'Alice'  : {'Betty'},
                'Robert' : set()
              }

    fof = {
            'Fred'  : {'Alice'},
            'Betty' : {'Fred'},
            'Wilma' : {'Betty', 'Robert'},
            'Alice' : {'Wilma'},
            'Robert': set()
          }
    friends2 = copy.deepcopy(friends) # Used to verify function is nonmutating
    assert(friendsOfFriends(friends) == fof)
    # Verify that the function is nonmutating:
    assert(friends == friends2)

    friends = {
                'A' : {'B'},
                'B' : {'C'},
                'C' : {'A'}
              }

    fof = {
            'A' : {'C'},
            'B' : {'A'},
            'C' : {'B'}
          }
    assert(friendsOfFriends(friends) == fof)

    friends = {
                'Melissa' : {'Joshua', 'Anna'},
                'Joshua' : {'Orelia'},
                'Anna' : {'Cynthia'},
                'Orelia' : set(),
                'Cynthia' : set()
              }

    fof = {
            'Melissa': {'Orelia', 'Cynthia'},
            'Joshua': set(),
            'Anna': set(),
            'Orelia': set(),
            'Cynthia': set()
          }
    assert(friendsOfFriends(friends) == fof)

    assert(friendsOfFriends(dict()) == dict())


def main():
    testFriendsOfFriends()

main()
