from cmu_cpcs_utils import testFunction
import copy

def getHoursLogged(logs):
    result=dict()
    for time, name in logs:
        if name not in result:
            result[name]=time
        else:
            result[name]=time-result[name]
    return result

@testFunction
def testGetHoursLogged():
    logs1 = [(0, 'Spongebob'), (10, 'Krabs'), (30, 'Squidward'),
             (55, 'Krabs'), (250, 'Squidward'), (300, 'Spongebob')]
    assert(getHoursLogged(logs1) ==
        {'Spongebob': 300, 'Krabs': 45, 'Squidward': 220})

    logs2 = [(10, 'A'), (20, 'A')]
    assert(getHoursLogged(logs2) == {'A': 10})

    logs3 = [(10, 'A'), (20, 'A'), (21, 'B'), (22, 'B')]
    assert(getHoursLogged(logs3) == {'A': 10, 'B': 1})

    assert(getHoursLogged([]) == dict())

    # Verify that the function is nonmutating:
    L = [(10, 'A'), (20, 'A')]
    getHoursLogged(L)
    assert(L == [(10, 'A'), (20, 'A')])

def main():
    testGetHoursLogged()

main()
