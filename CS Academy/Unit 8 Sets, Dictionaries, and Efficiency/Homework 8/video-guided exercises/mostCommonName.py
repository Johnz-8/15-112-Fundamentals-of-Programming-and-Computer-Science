from cmu_cpcs_utils import testFunction

def getCounts(L):
    counts=dict()
    for name in L:
        if name not in counts:
            counts[name]=1
        else:
            counts[name]+=1
    return counts

def mostCommonName(names):
    maxCount=0
    counts=getCounts(names)
    mostCommonName=set()
    for name in counts:
        currentCount=counts[name]
        if currentCount>maxCount:
            maxCount=currentCount
            mostCommonName=set([name])
        if currentCount==maxCount:
            mostCommonName.add(name)
    
    if len(names)==0:
        return None
    elif len(mostCommonName)==1:
        return mostCommonName.pop()
    else:
        return mostCommonName

@testFunction
def testGetCounts():
    L = ['Jane', 'Aaron', 'Cindy', 'Aaron']
    assert(getCounts(L) == {'Jane': 1, 'Aaron': 2, 'Cindy': 1})

    L = ['Jane', 'Aaron', 'Cindy', 'Aaron', 'Jane']
    assert(getCounts(L) == {'Jane': 2, 'Aaron': 2, 'Cindy': 1})

    # Verify that the function is nonmutating:
    L = ['Jane', 'Aaron', 'Cindy', 'Aaron']
    getCounts(L)
    assert(L == ['Jane', 'Aaron', 'Cindy', 'Aaron'])

@testFunction
def testMostCommonName():
    L = ['Jane', 'Aaron', 'Cindy', 'Aaron']
    assert(mostCommonName(L) == 'Aaron')

    L = ['Jane', 'Aaron', 'Cindy', 'Aaron', 'Jane']
    assert(mostCommonName(L) == {'Jane', 'Aaron'})

    assert(mostCommonName([]) == None)

    # Verify that the function is nonmutating:
    L = ['Jane', 'Aaron', 'Cindy', 'Aaron']
    mostCommonName(L)
    assert(L == ['Jane', 'Aaron', 'Cindy', 'Aaron'])

def main():
    testGetCounts()
    testMostCommonName()

main()
