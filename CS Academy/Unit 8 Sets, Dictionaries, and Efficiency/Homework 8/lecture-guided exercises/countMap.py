from cmu_cpcs_utils import testFunction

def countMap(L):
    counts=dict()
    for S in L:
        for v in S:
            if v not in counts:
                counts[v]=1
            else:
                counts[v]+=1
    
    res=dict()
    for k in counts:
        v = counts[k]
        if v not in res:
            res[v]={k}
        else:
            res[v].add(k)
    return res

@testFunction
def testCountMap():
    L = [ {'a', 'b'}, {'a', 'c'}, {'a', 'b', 'd'} ]   
    d = { 1: {'c', 'd'}, 
          2: {'b'}, 
          3: {'a'} }
    assert(countMap(L) == d)

    L = [ {'d'}, {'x', 'y'} ]
    d = { 1: {'d', 'x', 'y'} }
    assert(countMap(L) == d)

    L = [ {1, 'a'}, {2, 'a'} ]
    d = { 1: {1, 2}, 
          2: {'a'} }
    assert(countMap(L) == d)
    
    L = [ {5, 4.4, 'a'}, {4.4, 'b', ('a', 'b')} ]
    d = { 1: {5, 'a', 'b', ('a', 'b')}, 
          2: {4.4} }
    assert(countMap(L) == d)

    assert(countMap([]) == dict())


def main():
    testCountMap()

main()
