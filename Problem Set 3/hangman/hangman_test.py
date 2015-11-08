# 6.00 Problem Set 3
# 
# Hangman game - Unit Testing
#

from unittest import TestCase
import hangman
import hangman_solution


class HangmanIsWordGuessed(TestCase):
    def setUp(self):
        pass

    def assertWithSolution(self, secret_word, letters_guessed):
        self.assertEquals(hangman_solution.is_word_guessed(secret_word, letters_guessed),
                          hangman.is_word_guessed(secret_word, letters_guessed))

    def test1(self):
        secret_word = "apple"
        letters_guessed = ['a', 'e', 'i', 'k', 'p', 'r', 's']
        self.assertWithSolution(secret_word, letters_guessed)

    def test2(self):
        secret_word = "durian"
        letters_guessed = ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']
        self.assertWithSolution(secret_word, letters_guessed)
