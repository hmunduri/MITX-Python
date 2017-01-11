__author__ = 'm'

"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""


def count_bobs(string):
    keyword = "bob"
    keyword_length = len(keyword)
    counter = 0
    for index in range(len(string) - keyword_length + 1):
        if string[index:index + keyword_length] == keyword:
            counter += 1
    return counter


def main():
    s = input("Enter a string: ")
    print("Number of times bob occurs is: " + str(count_bobs(s)))


if __name__ == "__main__":
    main()
