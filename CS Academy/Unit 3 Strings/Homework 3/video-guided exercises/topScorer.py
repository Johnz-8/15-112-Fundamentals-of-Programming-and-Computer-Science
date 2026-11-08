from cmu_cpcs_utils import testFunction

def topScorer(data):
    champScore=-1
    champPlayer=None
    for line in data.splitlines():
        firstCommaIdx=line.find(',')
        currPlayer=line[:firstCommaIdx]
        scores=line[firstCommaIdx+1:]
        currScore=0
        for score in scores.split(','):
            currScore+=int(score)
        if currScore>champScore:
            champPlayer=currPlayer
            champScore=currScore
        elif currScore==champScore:
            champPlayer=champPlayer+','+currPlayer
    return champPlayer

@testFunction
def testTopScorer():
    data = '''\
Joe,10,20,30,40
Lauren,10,20,30
Ben,10,20,30,5
'''
    assert(topScorer(data) == 'Joe')

    data = '''\
David,11,20,30
Austin,10,20,30,1
Lauren,50
'''
    assert(topScorer(data) == 'David,Austin')

    data = '''\
Ping-Ya,100,80,90
'''
    assert(topScorer(data) == 'Ping-Ya')

    data = '''\
Reyna,20,40,40
Ema,5,5,5,5,10
Ketandu,50,20,10,20
Tanya,80,20
Kate,70
'''
    assert(topScorer(data) == 'Reyna,Ketandu,Tanya')

    assert(topScorer('') == None)


def main():
    testTopScorer()

main()
