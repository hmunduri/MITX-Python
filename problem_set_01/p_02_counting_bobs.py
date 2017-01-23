__author__ = 'm'

"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2

Two solutions are provided. The former solution 'count_bobs' uses a for loop,
while the latter one 'count_bobs_comprehension' uses a Python feature called
comprehension which is widely used by Pythonistas.
"""


def count_bobs(s: str) -> int:
    """
    :param s: a string
    :return: the number of bobs in s
    """
    bob = 'bob'
    bob_len = len(bob)
    counter = 0

    for i in range(len(s) - bob_len + 1):
        if s[i:i + bob_len] == bob:
            counter += 1

    return counter


def count_bobs_comprehension(s: str) -> int:
    """
    :param s: a string
    :return: the number of bobs in s
    """
    bob = 'bob'
    bob_len = len(bob)

    return len([bob for i in range(len(s) - bob_len + 1)
                if s[i:i + bob_len] == bob])

def main():
    s = input('Enter a string: ')
    print('Number of times bob occurs is:', str(count_bobs(s)))
    print('Number of times bob occurs is (using comprehension):',
          str(count_bobs_comprehension(s)))


if __name__ == '__main__':
    main()
