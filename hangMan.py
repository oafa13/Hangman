import random
from words import wordList

def getWord():
    word = random.choice(wordList)  # We gonna assign the wordList to word and we gonna mix them.
    return word.lower()             # We gonna return the words to lower.

def play(word):
    guessed = False
    guessedLetters = []             # Here we are storing all used Letters.
    tries = 8                       # Here we are setting how many tries will the player have.
    wordCompl = "_"*len(word)       # Here we will replace the word with -> _
    print('Lets play Hangman!')
    print(wordCompl)

    while not guessed and tries > 0:
        guess = input('Guess a Letter: ').lower()
        if len(guess) == 1 and guess.isalpha():         # We are making sure that the guess is 1 and its a character.
            if guess in guessedLetters:                 # We are checking if the guessed Letter has been already used.
                print('That letter has already been used!')
                print(wordCompl)
            elif guess not in word:                     # We are checking if the guessed Letter is not in the word.
                print(guess, ' is not in the word!')
                guessedLetters.append(guess)            # We are adding the letter to the guessed Letters.
                tries -= 1                              # We are taking one life.
                print(wordCompl)
            else:
                print(guess, ' is in the word.')
                guessedLetters.append(guess)            # We are adding the guessed letter to the guessedLetters Storage.
                shrededWord = list(wordCompl)           # We gonna assign the wordCmpl to shrededWord as list.
                multiInd = [a for a, letter in enumerate(word) if letter == guess]  # Here we are making a function that checks if the guessed letter is in the word.
                for ind in multiInd:        # Here we are checking for every character in the word.
                    shrededWord[ind] = guess    # We are assigning the character to the shrededWord if its the guess.
                wordCompl = ''.join(shrededWord)    # We are joining the wordCompl with shrededWord becouse we want the '_' to be replaced with the guessed character.
                if '_' not in wordCompl:        # We are making sure that if there are no more '_'.
                    guessed = True              # If there are no more '_' that means that the word is guessed.
                print(wordCompl)
    if guessed:
        print('Congrats! You guessed the Word!')
    else:
        print('You failed! The word was ' + word)


def main():
    word = getWord()
    play(word)

if __name__ == "__main__":
    main()
