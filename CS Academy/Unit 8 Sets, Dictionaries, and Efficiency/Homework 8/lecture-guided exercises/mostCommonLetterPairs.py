from cmu_cpcs_utils import testFunction
def letterPairsDict(text):
    text=text.lower()
    res=dict()
    for i in range(len(text)-1):
        pair=text[i:i+2]
        if pair.isalpha():
            res[pair]=res.get(pair,0)+1
    return res

def mostCommonLetterPairs(text, n):
    res=dict()
    letterPairs=letterPairsDict(text)
    counts=list(letterPairs.values())
    counts.sort()
    counts.reverse()
    if n>len(counts):
        return f"{n} is too large"
    
    threshold=counts[n-1]
    for key in letterPairs:
        if letterPairs[key]>=threshold:
            res[key]=letterPairs[key]
    return res

@testFunction
def testMostCommonLetterPairs():
    assert(mostCommonLetterPairs('abcbc', 1) == { 'bc':2 })
    assert(mostCommonLetterPairs('abcbc', 2) == { 'bc':2, 'ab':1, 'cb':1 })
    assert(mostCommonLetterPairs('abcbc', 3) == { 'bc':2, 'ab':1, 'cb':1 })
    assert(mostCommonLetterPairs('abcbc', 4) == '4 is too large')
    text = '''
    "Optimism is the faith that leads to achievement.
    Nothing can be done without hope and confidence."
        -- HELEN KELLER
    '''
    assert(mostCommonLetterPairs(text, 1) == { 'th': 5 })
    assert(mostCommonLetterPairs(text, 2) == { 'th': 5, 'le': 3, 'en': 3})


def main():
    testMostCommonLetterPairs()

main()
