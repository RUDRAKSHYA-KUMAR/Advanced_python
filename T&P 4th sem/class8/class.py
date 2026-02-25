#pythons set- a set of unique elements , means elements within a set can not be duplicated
"""
characteristics of set:
1. unordered collection of items    
2. mutable- we can add or remove elements from a set
3. no duplicate elements allowed
4. elements of a set are immutable (cannot be changed)
5. sets can contain heterogeneous elements (different data types)
6. sets support mathematical operations like union, intersection, difference, etc.
7. sets are defined using curly braces {} or the set() constructor

"""

#empty set can not be created using {}, as it will create an empty dictionary
#we can not perform index based operations on sets as they are unordered

my_set = {"mango", "ram", True, 1 }
print("Original set:", my_set)
print([x**2 for x in range(10) if x%2==0])

"""Questons Homwork:
1. write a program to take a string input from the user and print it in reverse
2. count the number of uppercase and lower case character in a string.
3. check whether the given string contains only digits
4. replace all the space with underscore in a string
5. count the frequency of each character in a string
6. find the first and last occurance of a character in a strring
7. remove all vowel from a string
8. check two strings are anagram or not
9. capitalise the first letter of each word in a string
10. check whether a string is palindrome or not without using built in reverse function"""