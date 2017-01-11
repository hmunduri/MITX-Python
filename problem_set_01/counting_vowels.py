__author__ = 'm'

"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""


def count_vowels(s: str) -> int:
    counter = 0
    for c in s:
        if c in 'aeiou':
            counter += 1
    return counter


def main():
    s = input('Enter a string: ')
    print('Number of vowels:', str(count_vowels(s)))


if __name__ == '__main__':
    main()
