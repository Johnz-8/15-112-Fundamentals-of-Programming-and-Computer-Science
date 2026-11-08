from cmu_cpcs_utils import testFunction

def invertDictionary(d):
    result=dict()
    for key in d:
        previousValue=d[key]
        if previousValue not in result:
            result[previousValue]=set([key])
        else:
            result[previousValue].add(key)
    return result

@testFunction
def testInvertDictionary():
    d = {'Chicago' : 'IL', 'Pittsburgh' : 'PA', 'Philadelphia' : 'PA'}
    inverted = {'IL' : {'Chicago'}, 'PA' : {'Pittsburgh', 'Philadelphia'}}
    assert(invertDictionary(d) == inverted)
    # Verify that the function is nonmutating:
    assert(d == {'Chicago' : 'IL', 'Pittsburgh' : 'PA', 'Philadelphia' : 'PA'})

    d = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd'}
    inverted = {'a' : {1}, 'b' : {2}, 'c' : {3}, 'd' : {4}}
    assert(invertDictionary(d) == inverted)

    d = {'x' : 5, 'y' : 5, 'z' : 5}
    inverted = {5 : {'x', 'y', 'z'}}
    assert(invertDictionary(d) == inverted)

    assert(invertDictionary(dict()) == dict())

def main():
    testInvertDictionary()

main()
