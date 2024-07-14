""" Given a string of lowercase letters in the range ascii[a-z], determine the index of a character that can be removed to make the string a palindrome. There may be more than one solution, but any will do. If the word is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove.

Example

Either remove 'b' at index  or 'c' at index .

Function Description

Complete the palindromeIndex function in the editor below.

palindromeIndex has the following parameter(s):

string s: a string to analyze
Returns

int: the index of the character to remove or 
Input Format

The first line contains an integer , the number of queries.
Each of the next  lines contains a query string .

Constraints

All characters are in the range ascii[a-z].
Sample Input

STDIN   Function
-----   --------
3       q = 3
aaab    s = 'aaab' (first query)
baa     s = 'baa'  (second query)
aaa     s = 'aaa'  (third query)
Sample Output

3
0
-1
Explanation

Query 1: "aaab"
Removing 'b' at index  results in a palindrome, so return .

Query 2: "baa"
Removing 'b' at index  results in a palindrome, so return .

Query 3: "aaa"
This string is already a palindrome, so return . Removing any one of the characters would result in a palindrome, but this test comes first.

Note: The custom checker logic for this challenge is available here."""
#!/bin/python3

# Importing necessary modules
import math
import os
import random
import re
import sys

# Function to check if a given string is a palindrome
def is_palindrome(s):
    for i in range(len(s)//2):
        # Compare characters from both ends of the string
        if s[i] != s[len(s)-i-1]:
            return False
    
    # If the loop completes without returning, the string is a palindrome
    return True

# Function to find the index of a character whose removal makes the string a palindrome
def palindromeIndex(s):
    for i in range(len(s)//2):
        j = len(s)-i-1
        # Check if characters at positions i and j are not equal
        if s[i] != s[j]:
            # Check if removing character at position i makes the remaining string a palindrome
            if is_palindrome(s[0:i] + s[i+1:]):
                return i
            # Check if removing character at position j makes the remaining string a palindrome
            elif is_palindrome(s[0:j] + s[j+1:]):
                return j
    
    # If no such index is found, return -1
    return -1

# Main block
if __name__ == '__main__':
    # Open a file for writing output
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Input the number of test cases
    q = int(input().strip())

    # Loop through each test case
    for q_itr in range(q):
        # Input the string for each test case
        s = input()

        # Call the palindromeIndex function and write the result to the output file
        result = palindromeIndex(s)
        fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()
