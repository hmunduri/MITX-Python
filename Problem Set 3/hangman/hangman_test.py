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

    def assert_solution(self, secret_word, letters_guessed):
        self.assertEquals(hangman_solution.is_word_guessed(secret_word, letters_guessed),
                          hangman.is_word_guessed(secret_word, letters_guessed))

    def test_1(self):
        secret_word = "apple"
        letters_guessed = ['a', 'e', 'i', 'k', 'p', 'r', 's']
        self.assert_solution(secret_word, letters_guessed)

    def test_2(self):
        secret_word = "durian"
        letters_guessed = ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']
        self.assert_solution(secret_word, letters_guessed)

    def random_test_1(self):
        secret_word = "coconut"
        letters_guessed = ['p', 'n', 'l', 't', 'r', 'k', 'd', 'w', 'm', 'f']
        self.assert_solution(secret_word, letters_guessed)

    def random_test_2(self):
        secret_word = "coconut"
        letters_guessed = ['z', 'h', 'v', 'n', 'b', 'm', 'e', 'u', 'j', 'k']
        self.assert_solution(secret_word, letters_guessed)

    def random_test_3(self):
        secret_word = "pineapple"
        letters_guessed = []
        self.assert_solution(secret_word, letters_guessed)

    def random_test_4(self):
        secret_word = "banana"
        letters_guessed = ['z', 'x', 'q', 'b', 'a', 'n', 'a', 'n', 'a']
        self.assert_solution(secret_word, letters_guessed)
