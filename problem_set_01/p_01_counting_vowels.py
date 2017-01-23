__author__ = 'm'

"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5

Two possible solutions are provided. The former 'count_vowels' is a solution
that uses a for loop. The latter 'count_vowels_comprehension' uses a Python
feature called comprehension which use widely used between Pythonistas.
"""


def count_vowels(s: str) -> int:
    """
    :param s: a string
    :return: the number of vowels in s
    """
    counter = 0
    for c in s:
        if c in 'aeiou':
            counter += 1
    return counter

def count_vowels_comprehension(s: str) -> int:
    """
    :param s: a string
    :return: the number of vowels in s
    """
    return len([v for v in s if v in 'aeiou'])


def main() -> None:
    s = input('Enter a string: ')
    print('Number of vowels:', str(count_vowels(s)))
    print('Number of vowels (using comprehension):', str(count_vowels_comprehension(s)))


if __name__ == '__main__':
    main()
