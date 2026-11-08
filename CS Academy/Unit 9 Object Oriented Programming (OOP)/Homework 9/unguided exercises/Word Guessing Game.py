from cmu_cpcs_utils import testFunction

class WordGuessingGame:
    def __init__(self, word):
        self.word=word
        self.guessCount=0
        self.guessedLetters=[]

    def getDisplayWord(self):
        result=''
        for c in self.word:
            if c in self.guessedLetters:
                result+=c
            else:
                result+='-'
        return result
        
    def guessLetter(self, guessLetter):
        if self.isGameOver():
            return
        self.guessCount+=1
        if guessLetter not in self.guessedLetters:
            self.guessedLetters.append(guessLetter)
            self.guessedLetters.sort()

    def isGameOver(self):
        for c in self.word:
            if c not in self.guessedLetters:
                return False
        return True

@testFunction
def testWordGuessingGameClass():
    game1 = WordGuessingGame('SALSA')
    assert(game1.guessCount == 0)
    assert(game1.guessedLetters == [ ]) # a sorted list of the guessed letters
    assert(game1.getDisplayWord() == '-----') # the target word, but with '-'
                                              # in place of unguessed letters
    assert(game1.isGameOver() == False) 

    game1.guessLetter('A')
    assert(game1.guessCount == 1)
    assert(game1.guessedLetters == ['A'])
    assert(game1.getDisplayWord() == '-A--A')
    assert(game1.isGameOver() == False)

    game1.guessLetter('X')
    assert(game1.guessCount == 2)
    assert(game1.guessedLetters == ['A', 'X'])
    assert(game1.getDisplayWord() == '-A--A')
    assert(game1.isGameOver() == False)

    game1.guessLetter('X') # guessed again!
    assert(game1.guessCount == 3)
    assert(game1.guessedLetters == ['A', 'X'])
    assert(game1.getDisplayWord() == '-A--A')
    assert(game1.isGameOver() == False)

    game1.guessLetter('S')
    assert(game1.guessCount == 4)
    assert(game1.guessedLetters == ['A', 'S', 'X'])
    assert(game1.getDisplayWord() == 'SA-SA')
    assert(game1.isGameOver() == False)

    game1.guessLetter('L')
    assert(game1.guessCount == 5)
    assert(game1.guessedLetters == ['A', 'L', 'S', 'X'])
    assert(game1.getDisplayWord() == 'SALSA')
    # The game is over because the entire word has been guessed
    assert(game1.isGameOver() == True)
    
    # Since the game is over, any additional guesses do not count
    game1.guessLetter('Z')
    assert(game1.guessCount == 5)
    assert(game1.guessedLetters == ['A', 'L', 'S', 'X'])
    assert(game1.getDisplayWord() == 'SALSA')
    assert(game1.isGameOver() == True)

def main():
    testWordGuessingGameClass()

main()
