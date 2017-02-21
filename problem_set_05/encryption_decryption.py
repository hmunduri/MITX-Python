# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string


### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list


### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(' !@#$%^&*()-_+={}[]|\:;\'<>?,./"')
    return word in word_list


### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open('story.txt')
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'


class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        pass  # delete this line and replace with your code here

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        pass  # delete this line and replace with your code here


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less
        code is repeated
        '''
        pass  # delete this line and replace with your code here

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        pass  # delete this line and replace with your code here

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class

        Returns: a COPY of self.encrypting_dict
        '''
        pass  # delete this line and replace with your code here

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        pass  # delete this line and replace with your code here

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift (ie. self.encrypting_dict and
        message_text_encrypted).

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        pass  # delete this line and replace with your code here


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        pass  # delete this line and replace with your code here

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        pass  # delete this line and replace with your code here


#
# Problem 1: Encryption
#

def shift_lower_case_letters(shifted_dictionary, shift):
    lower_case_letters = string.ascii_lowercase
    for i in range(len(lower_case_letters)):
        shifted_dictionary[lower_case_letters[i]] = lower_case_letters[(i + shift) % len(lower_case_letters)]


def shift_upper_case_letters(shifted_dictionary, shift):
    upper_case_letters = string.ascii_uppercase
    for i in range(len(upper_case_letters)):
        shifted_dictionary[upper_case_letters[i]] = upper_case_letters[(i + shift) % len(upper_case_letters)]


def build_coder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    :param shift: 0 <= int < 26
    :returns: dict
    """
    shifted_dictionary = {}
    shift_lower_case_letters(shifted_dictionary, shift)
    shift_upper_case_letters(shifted_dictionary, shift)

    return shifted_dictionary


def apply_coder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    :param text: string
    :param coder: dict with mappings of characters to shifted characters
    :returns: text after mapping coder chars to original text
    """
    cyphertext = ''

    for letter in text:
        if letter in string.ascii_letters:
            cyphertext += coder[letter]
        else:
            cyphertext += letter

    return cyphertext


def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    :param text: string to apply the shift to
    :param shift: amount to shift the text (0 <= int < 26)
    :returns: text after being shifted by specified amount.
    """
    return apply_coder(text, build_coder(shift))


def get_number_of_valid_words(words, word_list):
    number_of_valid_words = 0

    for word in words:
        if is_word(word_list, word):
            number_of_valid_words += 1

    return number_of_valid_words


#
# Problem 2: Decryption
#
def find_best_shift(word_list, text):
    """
    Finds a shift key that can decrypt the encoded text.

    :param word_list: a lists of words
    :param text: string
    :returns: 0 <= int < 26
    """
    best_shift = 0
    max_number_of_valid_words = 0

    for shift in range(26):
        deciphered_text = apply_shift(text, shift)
        words = deciphered_text.split()
        number_of_valid_words = get_number_of_valid_words(words, word_list)

        if number_of_valid_words > max_number_of_valid_words:
            best_shift = shift
            max_number_of_valid_words = number_of_valid_words

    return best_shift


def decrypt_story():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function get_story_string().
    Use the functions get_story_string and loadWords to get the
    raw data you need.

    :returns: string - story in plain text
    """
    story = get_story_string()
    word_list = load_words()
    best_shift = find_best_shift(word_list, story)

    return apply_shift(story, best_shift)


#
# Build data structures used for entire session and run encryption
#

def main():
    print(decrypt_story())


if __name__ == '__main__':
    main()
