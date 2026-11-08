from cmu_cpcs_utils import testFunction

def differByOneLetter(word1, word2):
    count=0
    for c in range(len(word1)):
        if word1[c]!=word2[c]:
            count+=1
    if count!=1:
        return False
    return True

def isWordLadder(s):
    allPrevWord=''
    prevWord=''
    if s==''or ('-'not in s):
        return False

    for word in s.split('-'):
        if word=='':
            return False
        if prevWord=='':
            prevWord=word
            allPrevWord+=word+'-'
            continue
        if len(word)!=len(prevWord):
            return False

        if not differByOneLetter(word,prevWord):
            return False

        if allPrevWord.count(word)>0:
            return False
        prevWord=word
        allPrevWord+=word+'-'
    return True

@testFunction
def testIsWordLadder():
    assert(isWordLadder('dog-cog-cot-cat') == True)
    assert(isWordLadder('cat-bat') == True)
    assert(isWordLadder('cold-cord-card-ward-warm') == True)
    assert(isWordLadder('toggle-goggle-google') == True)
    assert(isWordLadder('cold-cord-card-warm') == False)
    assert(isWordLadder('cat-bat-cat') == False) # duplicate word
    assert(isWordLadder('cat-bat-') == False)
    assert(isWordLadder('cat-cats') == False)
    assert(isWordLadder('cat-cabs') == False)
    assert(isWordLadder('cat') == False) # just one word
    assert(isWordLadder('') == False) # no words
    assert(isWordLadder('-') == False) # no words

def main():
    testIsWordLadder()

main()
