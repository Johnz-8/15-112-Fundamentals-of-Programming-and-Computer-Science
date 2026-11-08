from cmu_cpcs_utils import testFunction

def makeSpeciesDictionary(animalData):
    result=dict()
    for line in animalData.splitlines():
        species=line.split(',')[0]
        breed=line.split(',')[1]
        name=line.split(',')[2]
        if species not in result:
            result[species]=dict()
            result[species][breed]=set([name])
            continue
        if breed not in result[species]:
            result[species][breed]=set([name])
        else:
            result[species][breed].add(name)

    return result

@testFunction
def testMakeSpeciesDictionary():
    animalData = '''\
dog,labrador,fred
cat,persian,betty
dog,shepherd,barney
dog,labrador,fred
dog,labrador,wilma
'''
    result = {
                'dog' :
                        {
                          'labrador' : {'fred', 'wilma'},
                          'shepherd' : {'barney'}
                        },
                'cat' :
                        {
                          'persian' : {'betty'}
                        }
             }
    assert(makeSpeciesDictionary(animalData) == result)

    assert(makeSpeciesDictionary("") == dict())


def main():
    testMakeSpeciesDictionary()

main()
