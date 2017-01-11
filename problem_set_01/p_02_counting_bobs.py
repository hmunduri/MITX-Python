__author__ = 'm'

"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""


def count_bobs(s: str) -> int:
    bob = "bob"
    bob_len = len(bob)
    counter = 0
    for i in range(len(s) - bob_len + 1):
        if s[i:i + bob_len] == bob:
            counter += 1
    return counter


def main():
    s = input("Enter a string: ")
    print("Number of times bob occurs is: " + str(count_bobs(s)))


if __name__ == "__main__":
    main()
