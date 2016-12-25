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

    def test_3(self):
        secret_word = "coconut"
        letters_guessed = ['p', 'n', 'l', 't', 'r', 'k', 'd', 'w', 'm', 'f']
        self.assert_solution(secret_word, letters_guessed)

    def test_4(self):
        secret_word = "coconut"
        letters_guessed = ['z', 'h', 'v', 'n', 'b', 'm', 'e', 'u', 'j', 'k']
        self.assert_solution(secret_word, letters_guessed)

    def test_5(self):
        secret_word = "pineapple"
        letters_guessed = []
        self.assert_solution(secret_word, letters_guessed)

    def test_6(self):
        secret_word = "banana"
        letters_guessed = ['z', 'x', 'q', 'b', 'a', 'n', 'a', 'n', 'a']
        self.assert_solution(secret_word, letters_guessed)


class HangmanGetGuessedWord(TestCase):
    def setUp(self):
        pass

    def assert_solution(self, secret_word, letters_guessed):
        self.assertEquals(hangman_solution.get_guessed_word(secret_word, letters_guessed).replace(" ", ""),
                          hangman.get_guessed_word(secret_word, letters_guessed).replace(" ", ""))

    def test_1(self):
        secret_word = "apple"
        letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
        self.assert_solution(secret_word, letters_guessed)

    def test_2(self):
        secret_word = "durian"
        letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
        self.assert_solution(secret_word, letters_guessed)

    def test_3(self):
        secret_word = "broccoli"
        letters_guessed = ['x', 'g', 'm', 'a', 'd', 'c', 'v', 't', 'h', 'k']
        self.assert_solution(secret_word, letters_guessed)

    def test_4(self):
        secret_word = "grapefruit"
        letters_guessed = ['i', 'q', 'y', 'p', 'h', 'k', 'o', 'c', 'u', 'n']
        self.assert_solution(secret_word, letters_guessed)

    def test_5(self):
        secret_word = "lettuce"
        letters_guessed = []
        self.assert_solution(secret_word, letters_guessed)

    def test_6(self):
        secret_word = "coconut"
        letters_guessed = ['f', 'w', 'i', 'y', 'z', 'q', 'h', 'v', 'j', 'p']
        self.assert_solution(secret_word, letters_guessed)


class HangmanGetAvailableLetters(TestCase):
    def setUp(self):
        pass

    def assert_solution(self, letter_guessed):
        self.assertEquals(hangman_solution.get_available_letters(letter_guessed),
                          hangman.get_available_letters(letter_guessed))

    def test_1(self):
        letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
        self.assert_solution(letters_guessed)

    def test_2(self):
        letters_guessed = []
        self.assert_solution(letters_guessed)

    def test_3(self):
        letters_guessed = ['e', 'u']
        self.assert_solution(letters_guessed)

    def test_4(self):
        letters_guessed = ['r', 's', 'q', 'n']
        self.assert_solution(letters_guessed)

    def test_5(self):
        letters_guessed = ['b', 'x', 'z', 'e', 'd']
        self.assert_solution(letters_guessed)

    def test_6(self):
        letters_guessed = ['p', 'z', 'w', 'y']
        self.assert_solution(letters_guessed)
