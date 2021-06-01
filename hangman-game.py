#Impots
import random
from  wordlist import words
import string
from visual import lives_visual

#Checks of word selected at random is valid
def find_valid_word(words):
    word = random.choice(words) #chooses a random word form the list 

    #If word has space or hyphen in it a new word is picked
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    #Returns the upercase version of all its letters
    return word.upper()


def hangman():
    #Uppercase letters
    word = find_valid_word(words)
    word_letters = set(word) #unique letters in word 
    alphabet = set(string.ascii_uppercase) #already predefines set of capital letters from library - string 
    used_letters = set() #already guessed letters

    #Total lives 
    lives = 7

    #While lives greater than zero and length of set greater than zerp
    while len(word_letters) > 0 and lives > 0:
        
        #letters used and live sleft
        print('You have', lives, ' lives left and You have used these letters: ', ' '.join(used_letters))

        #Lambda expression that keeps track of already used letters
        word_list = [letter if letter in used_letters else '-' for letter in word ]
        #Prints the visual rep of number of lives left
        print(lives_visual[lives])
        print('Current word: ',' '.join(word_list) )
        user_letter = input('Guess a letter: ').upper()

        #Game logic
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            #When guessed wrong 
            else:
                lives = lives - 1
                print('\nYour letter,', user_letter, 'is not in the word.')
                
        #When using a already used letter or guesses letter
        elif user_letter in used_letters:
            print('\nYou have already guessed this letter: ')
        #Invalid Character
        else:
            print('\nInvalid chracter, Try again')

    #When player runs out of lives
    if lives == 0:
        print(lives_visual[lives])
        print('You died, sorry. The word was', word)
    #When player guesses correctly
    else:
        print(f"Yay, you guessed Correct, '{word}'")

if __name__ == '__main__':
    hangman()