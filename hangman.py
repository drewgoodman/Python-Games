# HANGMAN GAME
# © Drew Goodman 2019

from os import system, name

hangman_art = HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

game_state = True
victor = False
guesses = 0
max_guesses = 6
guess_bank = []


def screen_clear():
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

def valid_word(word_checked):
    for character in word_checked:
        if character.isalpha() == False:
            print("Must be a single word with no numbers or special characters.")
            return False
    if len(word_checked) > 8 or len(word_checked) < 3:
        print("Must be between 3 and 8 letters long.")
        return False
    return True

def valid_guess(word_checked):
    length = len(word_checked)
    for character in word_checked:
        if character.isalpha() == False:
            print("Must be letters.")
            return False
    if length !=1 and length < 3 or length > 8:
        print("Invalid number of letters")
        return False
    elif length == 1 and word_checked in guess_bank:
        print("You've already guessed that letter")
        return False
    return True


print("\nWELCOME TO HANGMAN!\n")
print(f"Player 1 can type out a word, and Player 2 can make up to {max_guesses} guesses at what the word can be.")
print("Player 2, please look away.")
word = input("Player 1, please type out a word and press Enter:  ").strip().upper()
letter_bank = ["_"]  * len(word)

while valid_word(word) == False:
    word = input("Please try again and press ENTER:  ").strip().upper()

input(f"\nThe word [{word}] will be used.\nPlease press ENTER to start the game and afterwards give control to Player 2:  ")


def render_board():
    screen_clear()
    print(hangman_art[guesses])
    print('  '.join(letter_bank))
    print(f"\nGUESSES: {guesses} / {max_guesses}")
    print(str(guess_bank).strip("[]"))


def guess_letter(guess):
    global guesses
    guess_bank.append(guess)
    if guess in word:
        i = 0
        while i < len(word):
            if word[i] == guess:
                letter_bank[i] = guess
            i += 1
    else:
        guesses += 1

def guess_word(guess):
    global game_state
    global victor
    global guesses
    if guess == word:
        print(f"{word}! You guessed it!")
        game_state = False
        victor = True
    else:
        input(f"Sorry, but {guess} isn't it. Press ENTER: ")
        guesses += 1
    


while game_state:
    render_board()
    if guesses == max_guesses:
        break
    guess = input(f"\nPlease enter a single letter to try and fill out spaces, or type out an entire {len(word)} letter word to attempt to guess and win:  ").strip().upper()
    while valid_guess(guess) == False:
        guess = input(f"\nPlease try again with a single letter or a {len(word)} letter word, then press ENTER:  ").strip().upper()
    guess_letter(guess) if len(guess) == 1 else guess_word(guess)

if victor:
    print(f"\nYes, the word was {word}! Player 2 wins!")
else:
    print("\nH A N G M A N")
    print(f"The word was {word}. Player 1 wins.")