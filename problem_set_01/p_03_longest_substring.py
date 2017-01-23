__author__ = 'm'

"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters
occur in alphabetical order. For example, if s = 'azcbobobegghakl',
then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd',
then your program should print

Longest substring in alphabetical order is: abc
"""


def get_longest_substring(s: str) -> str:
    """
    :param s: a string
    :return: the longest substring in alphabetical order
    """
    longest = current = s[0]
    for c in s[1:]:
        if c >= current[-1]:
            current += c
            if len(current) > len(longest):
                longest = current
        else:
            current = c
    return longest


def main():
    s = input('Enter a string: ')
    print('Longest substring in alphabetical order is:',
          get_longest_substring(s))

if __name__ == '__main__':
    main()
