import random

word = list()

def is_word_guessed(word, letters_guessed):
    for letter in word:
        if letter not in letters_guessed:
            return False
    return True

def welcomeScreen():
    name = input("Enter your name: ")
    print("WELCOME" +" " + name + " " + "TO SPACEMANS LAUNCH PAD!" )
    print("#################################################")

def load_word():
    f = open('dictionary.txt','r')
    words_list = f.readlines()
    f.close()
    # return random.choice(words).upper()
    words_list= words_list[0].split(' ')
    word = random.choice(words_list)
    return word


def letter_in_word(guess,word):
    for letter in word:
        if letter == guess:
            return True
    return False

def get_guessed_word(word, letters_guessed):
    already_guessed = []
    for letter in word:
        if letter in letters_guessed:
            already_guessed.append(letter)
        else:
            already_guessed.append(" _ ")
    return already_guessed


def try_again():
    ans = input("Would You Like To Try Again?: [Y = yes/ N = no]: ")
    if ans == 'Y' or ans == 'y':
        print("Here We Go!\n\n")
        return True
    elif ans == 'N' or ans == 'n':
        print('Hope You Enjoyed!')
        return False
    else:
        print("Come on now dont give me a hard time. Enter (Y or N)!!!!!!!!!!!!")

def spaceman(word):
    word_bank = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    tries = 7
    letters_guessed = list()
    print(word)

    while True:
        print('The word contains ' + str(len(word))+ ' letters.')
        guess = input("Enter one letter: ")
        if len(guess) != 1:
            print("invalid entry")

        if guess not in word_bank:
            print('You have already used this letter')
            print(' '.join(get_guessed_word(word, letters_guessed)))
            continue

        if guess in word_bank:
            word_bank.remove(guess)

        if letter_in_word(guess, word) == True:
            letters_guessed.append(guess)
            print("Correct! The letter you guessed appears in the word!\nWord Progress")
            print(''.join(get_guessed_word(word,letters_guessed)))

            if is_word_guessed(word,letters_guessed):
                print("Congratulations! You win.")
                print(f"Yes, the word is {word}!")
                break


            print("These are the letters that have not been guessed yet: " + ''.join(str(a) for a in word_bank))

        else:
            if tries == 0:
                print("++++++++++++++++++++++++++++++++++++++++++++++++\nYikes! You ran out of turns!\n\n[--Game Over--]\n=+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

            else:
                tries = tries - 1
                print(f"\nSorry guess again.\nYou have {tries + 1} incorrect guesses left!\nGuessed word so far: " + ''.join(get_guessed_word(word,letters_guessed)))
                print("Letters available: " + ''.join(str(a) for a in word_bank) + "\n")

welcomeScreen()

going = True
while going:
    spaceman(load_word())
    going = try_again()
