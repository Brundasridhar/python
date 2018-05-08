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


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    i=' '
    count=len(secretWord)
    for i in lettersGuessed:
        if(i in secretWord):
            count-=1
    if(count==0):
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
    count=len(secretWord)
    word=' '
    for i in secretWord:
        if(i in lettersGuessed):
            word=word+i+' '  
        else:
            word+='_ '
    return word

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alphabet=list(string.ascii_lowercase)
    i=' '
    x=0
    for i in lettersGuessed:
        x=alphabet.index(i)
        del(alphabet[x])
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

    
    '''
    import os
    k=0
    l=' '
    guess=[]
    print("Welcome to the game of Hangman")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n ")
    while(k<8):
        wavail=getAvailableLetters(guess)  
        print("You have", 8-k, "guesses left.")
        print("Available letters:",wavail)
        l=(str(input("Please enter your guess: "))).lower()
        if(len(l)==1):
            if(l not in guess):
                guess.append(l)
            if(l not in wavail):
                print("Oops! You've already guessed that letter:",getGuessedWord(secretWord, guess))
                print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  \n")
            elif(l in secretWord):
                print("Good guess:",getGuessedWord(secretWord, guess))
                print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
            elif(l not in secretWord):
                print("Oops! That letter is not in my word:",getGuessedWord(secretWord, guess))
                print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n ")
                k=k+1
            if('_' not in getGuessedWord(secretWord, guess)):
               break
        else:
            print("Please enter a single character only. Try again")
            
            
    if(isWordGuessed(secretWord, guess)==True):
        print('Congratulations, you won!')
    else:
        print("Game over.The word was " + secretWord)


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
input("Press <Enter> to continue")
exit

