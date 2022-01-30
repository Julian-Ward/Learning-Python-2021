# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    if getGuessedWord(secretWord, lettersGuessed) == secretWord:
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedWord = len(secretWord)*['_']
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            guessedWord[i] = secretWord[i]
    return ''.join(guessedWord)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    i=0
    while i<len(lettersGuessed) and lettersGuessed[i] in alphabet:
        alphabet.remove(lettersGuessed[i])
        i += 1
    print("Available letters: "+''.join(alphabet))
    return ''.join(alphabet)
        
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!\nI am thinking of a word that is " + str(len(secretWord)) + " long.")
    print("-------------")
    isGuessed = False
    allowedGuesses = 8
    guesses = 0
    lettersGuessed =[]
    
    #print("Secret word: " + secretWord)
    while isGuessed is False and guesses < 8:
        print("You have " + str(allowedGuesses-guesses) + " left.")
        available = getAvailableLetters(lettersGuessed)
        print("Available Letters: " + available)
        letter = input("Please guess a letter: ")
        if letter == '':
            letter = ' '
        elif len(letter) > 1:
            letter = letter[0]
        lettersGuessed += letter
        guessedWord = getGuessedWord(secretWord, lettersGuessed)
        guesses += 1
        
        if letter not in secretWord and letter in available:
            print("Oops! That letter is not in my word: " + guessedWord)
        elif letter not in available:
            print("Oops! You've already guessed that letter: " + guessedWord)
            guesses -= 1
        elif letter in secretWord:
            print("Good guess: " + guessedWord)
            guesses -=1
            
        isGuessed = isWordGuessed(secretWord, lettersGuessed)
        print("-------------")
        if len(lettersGuessed) == allowedGuesses and isGuessed == False:
            print("Sorry, you ran out of guesses. The word was " + secretWord + "." )
            break
    if isGuessed == True:
        print("Congratulations, you won!")
        
            






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

    
