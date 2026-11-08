from cmu_cpcs_utils import testFunction

def flightTimesMap(flightTimesString):
    res=dict()
    for line in flightTimesString.splitlines():
        terms=line.split(' ')
        departure=terms[2]
        arrival=terms[4]
        time=float(terms[6])
        if departure not in res:
            res[departure]={arrival:time}
        else:
            res[departure][arrival]=time
    return res

@testFunction
def testFlightTimesMap():
    ## Test 1 ##
    flightTimesString1 = '''\
Flying from Chicago to Seattle takes 4.75 hours.
Flying from Seattle to Chicago takes 4.0 hours.
Flying from Seattle to Pittsburgh takes 4.5 hours.
Flying from Pittsburgh to Chicago takes 1.67 hours.
'''
    flightTimesMap1 = {
        'Chicago': { 'Seattle': 4.75 },
        'Seattle': { 'Chicago': 4.0, 'Pittsburgh': 4.5 },
        'Pittsburgh': { 'Chicago' : 1.67 }
        }
    assert(flightTimesMap(flightTimesString1) == flightTimesMap1)


    ## Test 2 ##
    flightTimesString2 = '''\
Flying from Toronto to Vancouver takes 5.25 hours.
Flying from Ottawa to Montreal takes 0.8 hours.
'''
    flightTimesMap2 = {
        'Toronto': { 'Vancouver': 5.25 },
        'Ottawa': {'Montreal': 0.8 }
        }
    assert(flightTimesMap(flightTimesString2) == flightTimesMap2)


    ## Test 3 ##
    flightTimesString3 = '''\
Flying from London to Sydney takes 19.40 hours.
Flying from London to Paris takes 1.33 hours.
Flying from London to Tokyo takes 14.0 hours.
'''
    flightTimesMap3 = {
        'London': { 'Sydney': 19.40, 'Paris': 1.33, 'Tokyo': 14.0 },
        }
    assert(flightTimesMap(flightTimesString3) == flightTimesMap3)


    ## Test 4 ##
    assert(flightTimesMap('''''') == dict())

def main():
    testFlightTimesMap()

main()
