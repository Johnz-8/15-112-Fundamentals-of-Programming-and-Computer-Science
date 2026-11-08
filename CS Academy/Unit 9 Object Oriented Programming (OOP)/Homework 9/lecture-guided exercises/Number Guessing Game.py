from cmu_cpcs_utils import testFunction

class NumberGuessingGame:
    def __init__(self, target):
        self.target=target
        self.lo=1
        self.hi=100
        self.count=0
    
    def getPrompt(self):
        return f'Guess a number between {self.lo} and {self.hi}.'
    
    def guessNumber(self, guess):
        if guess<self.target:
            self.count+=1
            if guess>=self.lo:
                self.lo=guess+1
            return 'Too low!'
        
        elif guess>self.target:
            self.count+=1
            if guess<=self.hi:
                self.hi=guess-1
            return 'Too high!'
        
        else:
            self.count+=1
            if self.count==1:
                return 'You got it in 1 guess. Amazing!'
            else:
                return f'You got it in {self.count} guesses!'

@testFunction
def testNumberGuessingGameClass():
    game1 = NumberGuessingGame(35)
    assert(game1.target == 35)
    assert(game1.getPrompt() == 'Guess a number between 1 and 100.')

    # Guesses that are out of range do not change the potential range in the 
    # prompt, but still count as an attempted guess
    assert(game1.guessNumber(-1) == 'Too low!')
    assert(game1.getPrompt() == 'Guess a number between 1 and 100.')    

    # 50 is too high, so we know the new range of potential target numbers is 1
    # to 49 (inclusive)
    assert(game1.guessNumber(50) == 'Too high!')
    assert(game1.getPrompt() == 'Guess a number between 1 and 49.')

    assert(game1.guessNumber(30) == 'Too low!')
    assert(game1.getPrompt() == 'Guess a number between 31 and 49.')

    assert(game1.guessNumber(35) == 'You got it in 4 guesses!')

    game2 = NumberGuessingGame(84)
    assert(game2.target == 84)
    assert(game2.getPrompt() == 'Guess a number between 1 and 100.')

    # The win message includes "Amazing!" if only 1 guess was used
    assert(game2.guessNumber(84) == 'You got it in 1 guess. Amazing!')

    game3 = NumberGuessingGame(73)
    assert(game3.target == 73)
    assert(game3.getPrompt() == 'Guess a number between 1 and 100.')

    assert(game3.guessNumber(88) == 'Too high!')
    assert(game3.getPrompt() == 'Guess a number between 1 and 87.')

    # This guess is outside of our current potential range, so the prompt 
    # does not change
    assert(game3.guessNumber(90) == 'Too high!')
    assert(game3.getPrompt() == 'Guess a number between 1 and 87.')

    assert(game3.guessNumber(73) == 'You got it in 3 guesses!')
    
def main():
    testNumberGuessingGameClass()

main()
