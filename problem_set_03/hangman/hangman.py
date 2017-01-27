# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORD_LIST_FILENAME = 'words.txt'
NUMBER_OF_GUESSES = 8

# Helper Code
# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program


def load_words():
    """
    :returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print('Loading word list from file...')

    with open(WORD_LIST_FILENAME) as file:
        line = file.read()

    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')

    return word_list


def choose_word(word_list: [str]) -> str:
    """
    :param word_list: list of words (strings)

    :returns: a word from word_list at random
    """
    return random.choice(word_list)

# end of Helper Code
# -----------------------------------


def is_word_guessed(secret_word: str, letters_guessed: [str]) -> bool:
    """
    :param secret_word: string, the word the user is guessing
    :param letters_guessed: list, what letters have been guessed so far
    :returns: boolean, True if all the letters of secretWord are in
        lettersGuessed; False otherwise
    """
    return all(letter in letters_guessed for letter in secret_word)


def get_guessed_word(secret_word: str, letters_guessed: [str]) -> str:
    """
    :param secret_word: string, the word the user is guessing
    :param letters_guessed: list, what letters have been guessed so far
    :returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    return ' '.join(letter if letter in letters_guessed else '_'
                    for letter in secret_word)


def get_available_letters(letters_guessed: [str]) -> str:
    """
    :param letters_guessed: list, what letters have been guessed so far
    :returns: string, comprised of letters that represents what letters have
    not yet been guessed.
    """
    return ''.join(letter for letter in string.ascii_lowercase
                   if letter not in letters_guessed)


def print_header(word_len: int):
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(word_len))


def print_result(was_word_guessed: bool, secret_word: str):
    print_line_of_dashes()
    if was_word_guessed:
        print('Congratulations, you won!')
        return
    print('Sorry, you ran out of guesses. The word was {}.'
          .format(secret_word))


def print_line_of_dashes():
    print('-------------')


def play_game(secret_word: str) -> bool:
    """
    :param secret_word: secret word to be guessed
    :return: True if word was guessed, False otherwise.
    """
    guesses_left = NUMBER_OF_GUESSES
    letters_guessed = []

    while guesses_left > 0 and not is_word_guessed(secret_word,
                                                   letters_guessed):
        print_line_of_dashes()
        print('You have {} guesses left.'.format(guesses_left))
        print('Available letters: {}'.
              format(get_available_letters(letters_guessed)))

        letter_guessed = input('Please guess a letter: ').lower()

        if letter_guessed in letters_guessed:
            print("Oops! You've already guessed that letter: {}".
                  format(get_guessed_word(secret_word, letters_guessed)))
            continue

        letters_guessed.append(letter_guessed)

        if letter_guessed in secret_word:
            print('Good guess:', end=' ')
        else:
            print('Oops! That letter is not in my word:', end=' ')
            guesses_left -= 1

        print(get_guessed_word(secret_word, letters_guessed))

    return is_word_guessed(secret_word, letters_guessed)


def hangman(secret_word: str):
    """
    :param secret_word: string, the secret word to guess.

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
    """
    print_header(len(secret_word))
    game_result = play_game(secret_word)
    print_result(game_result, secret_word)


def main():
    word_list = load_words()
    secret_word = choose_word(word_list).lower()
    hangman(secret_word)


if __name__ == '__main__':
    main()
