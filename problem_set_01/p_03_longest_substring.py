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


def obtain_longest_substring(string):
    current_substring = longest_substring = string[0]
    for letter in string[1:]:
        if letter >= current_substring[-1]:
            current_substring += letter
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
        else:
            current_substring = letter
    return longest_substring


def main():
    s = input("Enter a string: ")
    print("Longest substring in alphabetical order is: " + obtain_longest_substring(s))

if __name__ == "__main__":
    main()
