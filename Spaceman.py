import random

letters_guessed = []

def welcomeScreen():
    name = input("Enter your name: ")
    print("WELCOME" +" " + name + " " + "TO SPACEMANS LAUNCH PAD!" )
    print("################################################")

    print()
welcomeScreen()

def load_word():
    f = open("dictionary.txt",'r')
    words = f.readlines()
    f.close()
    # return random.choice(words).upper()
    words= words[0].split(' ')
    word = random.choice(words).upper()
    return word



def check(word,guesses,guess):
    guess = guess.upper()
    status = ''
    i = 0
    matches = 0
    for letter in word:
        if letter in guesses:
            status+= letter
        else:
            status += '*'

def letter_in_word(guess,letter):

    if letter == guess:
        matches += 1

    if matches >= 1:
        print('Yes! The word contains the letter '  + guess + '.')
    else:
        print('Sorry. The word does not contain the letter ' + guess + '.')
        return status

def get_word(guess,guesses,word):
    guess = input(text)
    guess = guess.upper()
    if guess in guesses:
        print('You already guessed "' + guess + '"')
    elif len(guess) == len(word):
        guesses.append(guess)
        if guess == word:
            return False
        else:
            print('Sorry, that is incorrect.')
    elif len(guess) == 1:
        guesses.append(guess)
        result = check(word,guesses,guess)
        if result == word:
            return False

        else:
            print(result)
    else:
        print('invalid entry.')





def main():

    print('The word contains', len(word), 'letters.')
    while True:
        text = 'Please enter one letter or a ()-letter word. '.format(len(word))
        guesses = []
        if guesses == True:
            print("Congratulations! You win.")
            print('Yes, the word is' + word + '! You got it in'+ len(guesses) + 'tries.')
        elif len(guesses) > 6:
            print ("You Suck.")
            print( 'The word is'+ word + '! You lost after' + len(guesses)+ 'tries.')
        else:
            print ("You've guessed "+len(guesses)+ " times out of 7.")
main()




#     '''
#     # A function that reads a text file of words and randomly selects one to use as the secret word
#     #     from the list.
#     # Returns:
#     #        string: The secret word to be used in the spaceman guessing game
#     # '''
#     f = open('words.txt', 'r')
#     words_list = f.readlines()
#     f.close()
#
#     words_list = words_list[0].split(' ')
#     secret_word = random.choice(words_list)
#     return secret_word
#
# def is_word_guessed(secret_word, letters_guessed):
#     '''
#     A function that checks if all the letters of the secret word have been guessed.
#     Args:
#         secret_word (string): the random word the user is trying to guess.
#         letters_guessed (list of strings): list of letters that have been guessed so far.
#     Returns:
#         bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
#     '''
#     # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
#     pass
#
# def get_guessed_word(secret_word, letters_guessed):
#     '''
#     A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
#     Args:
#         secret_word (string): the random word the user is trying to guess.
#         letters_guessed (list of strings): list of letters that have been guessed so far.
#     Returns:
#         string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
#     '''
#
#     #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
#
#     pass
#
#
# def is_guess_in_word(guess, secret_word):
#     '''
#     A function to check if the guessed letter is in the secret word
#     Args:
#         guess (string): The letter the player guessed this round
#         secret_word (string): The secret word
#     Returns:
#         bool: True if the guess is in the secret_word, False otherwise
#     '''
#     #TODO: check if the letter guess is in the secret word
#
#     pass
#
#
#
#
# def spaceman(secret_word):
#     '''
#     A function that controls the game of spaceman. Will start spaceman in the command line.
#     Args:
#       secret_word (string): the secret word to guess.
#     '''
#
#
#     #TODO: show the player information about the game according to the project spec
#
#     #TODO: Ask the player to guess one letter per round and check that it is only one letter
#
#     #TODO: Check if the guessed letter is in the secret or not and give the player feedback
#
#     #TODO: show the guessed word so far
#
#     #TODO: check if the game has been won or lost
#
#
#
#
#
#
# #These function calls that will start the game
# secret_word = load_word()
# spaceman(load_word())
