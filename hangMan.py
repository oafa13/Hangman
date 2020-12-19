# hangMan.py

import random
from words import wordList

# We are making random expresioins 
expresions = ['Nice, ', 'Good Job, ', 'Great, ']
randomExpresion = random.choice(expresions) # We are getting random expresion with random.choice

def get_word():
    word = random.choice(wordList)  # We are getting random word from the wordList
    return word.lower()             

def play(word):
    wordCompl = "_" * len(word)     # We are replacing the word with the length of the word with _
    guessedWords = []               # Storing Guessed Words
    guessedLetters = []             # Storing Guessed Letters
    tries = 10                      # Tries
    guessed = False                    
    print('Lets play Hangman!')
    print(wordCompl)

    while not guessed and tries > 0:
        guess = input('Enter a word or a letter: ').lower()        # Taking a guess

        # Founds if the letters has been already used
        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                print("You already guessed the letter " + guess)
            
            # Checks if the guess is not the word.
            elif guess not in word:
                print(guess + ' is/ not in the word!')
                tries = tries - 1 # Takes one life 
                guessedLetters.append(guess)
                print(wordCompl)
            
            # Checks if the guess is the word & the _ to be replaced with the letter/word
            else:     
                print(randomExpresion, guess + ' is/in the word!')
                guessedLetters.append(guess)        # We are storing the guessed letters
                wordAsList = list(wordCompl)        # We shred the word into letters
                multiInd = [a for a, letter in enumerate(word) if letter == guess]  # We gonna check every character with [a for a] in guess
                for ind in multiInd:                                              # We gonna take the character, and we gonna pass it.
                    wordAsList[ind] = guess
                wordCompl = ''.join(wordAsList)         # Then we gonna join them
                if '_' not in wordCompl:                # And if we don't have any left spaces
                    guessed = True                      # - we fully guessed the word
                print(wordCompl)
        
    if guessed:
        print('Congratulations, you guessed the word.')
    else:
        print('You failed! The word was ' + word)

def main():
    word = get_word()
    play(word)

if __name__ == '__main__':
    main()
